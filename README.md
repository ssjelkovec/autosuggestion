# Naivni Bayes Autosuggestion

## Upute za instalaciju i pokretanje servera (Upute su za Windows)

U mapi gjde je kod napravite mapu `db` i u nju kopirajte datoku [`sve.txt`](https://drive.google.com/drive/folders/1LyybpbRay9vZbFnQcUquUdj3WblDglmV)

### Instalacija servera: ([official upute](https://flask.palletsprojects.com/en/1.1.x/installation/))
- Otvorite `powershell`
- Navigirajte se u direktorij koda
- Unesite sljedeće komande:
- `python3 -m venv venv`
- `venv\Scripts\activate`
- `pip install Flask`

### Pokretanje servera
- Postavite `env` varijablu
- `$env:FLASK_APP = "main.py"`
- `flask run`

Stranicu možete pristupiti na [`localhost:5000`](http://localhost:5000)

 
