# Flask Video Test Project

Aplikacja Flask do testowania jakości wideo.

## Instalacja

1. Zainstaluj zależności:
```bash
pip install -r requirements.txt
```

Lub bezpośrednio:
```bash
pip install Flask
```

## Uruchomienie

Uruchom aplikację jedną z poniższych metod:

### Metoda 1: Bezpośrednio z app.py
```bash
python app.py
```

### Metoda 2: Używając Flask CLI
```bash
flask run
```

Aplikacja będzie dostępna pod adresem: **http://127.0.0.1:5000** (lub http://localhost:5000)

## Struktura projektu

- `app.py` - główny plik aplikacji Flask
- `templates/index.html` - szablon strony testowej
- `static/videos/` - folder z plikami wideo do testowania (nie są w Git z powodu rozmiaru)
- `wyniki_testu.csv` - plik CSV z wynikami testów (tworzy się automatycznie)

## Uwaga o plikach wideo

Pliki wideo w folderze `static/videos/` są ignorowane przez Git (dodane do `.gitignore`) ze względu na duży rozmiar. 

Aby uruchomić projekt lokalnie, dodaj własne pliki wideo do folderu `static/videos/` w formacie `.mp4`.

