from flask import Flask, render_template, request, jsonify
import csv
import os

app = Flask(__name__)

VIDEO_FOLDER = "static/videos"
CSV_FILE = "wyniki_testu.csv"
CSV_HEADER = ["numer_użytkownika", "wiek", "plec", "gatunek", "nazwa_filmu", "urzadzenie", "ocena"]


def ensure_csv_header() -> None:
    """Ensure CSV exists and has the expected header."""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(CSV_HEADER)
        return

    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))

    if not rows:
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(CSV_HEADER)
        return

    if rows[0] == CSV_HEADER:
        return

    # Rewrite file with new header, padding old rows if necessary.
    normalized_rows = [CSV_HEADER]
    for row in rows[1:]:
        padded = row + [""] * (len(CSV_HEADER) - len(row))
        normalized_rows.append(padded[: len(CSV_HEADER)])

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(normalized_rows)


@app.route("/")
def index():
    ensure_csv_header()
    videos = sorted(os.listdir(VIDEO_FOLDER))
    return render_template("index.html", videos=videos)


@app.route("/save", methods=["POST"])
def save():
    data = request.json
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            data["tester"],
            data.get("age"),
            data.get("gender"),
            data.get("genre"),
            data["video"],
            data["device"],
            data["rating"]
        ])
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True)
