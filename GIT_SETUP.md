# Instrukcja wysłania projektu na GitHub/GitLab

## Krok 1: Inicjalizacja repozytorium Git

Otwórz terminal w folderze projektu i wykonaj:

```bash
git init
```

## Krok 2: Dodanie plików do Git

```bash
git add .
git commit -m "Initial commit - Flask video test project"
```

**Uwaga:** Pliki wideo z folderu `static/videos/` są automatycznie pominięte dzięki `.gitignore`.

## Krok 3: Utworzenie repozytorium na GitHub/GitLab

1. Zaloguj się na **GitHub.com** lub **GitLab.com**
2. Kliknij "New repository" / "Nowe repozytorium"
3. Podaj nazwę (np. `flask-video-test`)
4. **NIE zaznaczaj** "Initialize with README" (już mamy README)
5. Kliknij "Create repository"

## Krok 4: Połącz lokalne repozytorium z GitHub/GitLab

Po utworzeniu repozytorium, GitHub/GitLab pokaże Ci komendy. Wykonaj:

```bash
git remote add origin https://github.com/TWOJA_NAZWA/flask-video-test.git
git branch -M main
git push -u origin main
```

**Lub dla GitLab:**
```bash
git remote add origin https://gitlab.com/TWOJA_NAZWA/flask-video-test.git
git branch -M main
git push -u origin main
```

**Zastąp `TWOJA_NAZWA` swoją nazwą użytkownika!**

## W Visual Studio Code

Możesz też użyć wbudowanego interfejsu Git w VS Code:

1. Kliknij ikonę **Source Control** (Ctrl+Shift+G)
2. Kliknij **"Initialize Repository"** (jeśli jeszcze nie jest zainicjowane)
3. Kliknij **"+"** przy plikach, które chcesz dodać
4. Wpisz wiadomość commit (np. "Initial commit")
5. Kliknij ✓ aby commitować
6. Kliknij **"..."** → **"Publish Branch"** aby wysłać na GitHub/GitLab

## Alternatywa: Git LFS dla plików wideo

Jeśli **naprawdę** chcesz dodać pliki wideo do Git (niezalecane - są duże):

1. Zainstaluj Git LFS: https://git-lfs.github.com/
2. W terminalu:
```bash
git lfs install
git lfs track "*.mp4"
git add .gitattributes
git add static/videos/*.mp4
```

Ale lepiej jest **pominąć filmy** w `.gitignore` (już skonfigurowane).

