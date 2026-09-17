from flask import Flask, request, url_for, redirect, abort

app = Flask(__name__)

PRODUKTY = {
    1: "Laptop",
    2: "Myszka",
    3: "Klawiatura"
    }

@app.route("/")
def index():
    return "Strona główna"

@app.route("/o-nas")
def o_nas():
    return "Jesteśmy klasą 4 Technik Programista. Robimy Sklep."

@app.route("/kontakt")
def kontakt():
    return "Napisz: sklep@example.com"

@app.route("/tajne")
def tajne():
    return "Brak dostępu", 403

@app.route("/api/status")
def status():
    return {"ok": True, "wersja": "0.1"}

@app.route("/czesc/<imie>")
def czesc(imie):
    return f"Cześć, {imie}!"

@app.route("/uzytkownik/<imie>/<nazwisko>")
def uzytkownik(imie, nazwisko):
    return f"Użytkownik: {imie} {nazwisko}"

@app.route("/dodaj/<int:a>/<int:b>")
def dodaj(a, b):
    return f"{a} + {b} = {a + b}"

@app.route("/podziel/<int:a>/<int:b>")
def podziel(a, b):
    if b == 0:
        return "Nie dzielimy przez zero", 400
    return f"{a} / {b} = {a / b}"

@app.route("/powitanie")
def powitanie():
    imie = request.args.get("imie", "nieznajomy")
    godzina = request.args.get("gdozina", type=int)
    if godzina is not None and godzina < 12:
        return f"Dzień dobry, {imie}!"
    return f"Witaj, {imie}!"

@app.route("/linki")
def linki():
    return url_for("produkt", id=5)

@app.route("/stary-adres")
def stary():
    return redirect(url_for("index"))

@app.route("/produkt/<int:id>")
def produkt(id):
    if id not in PRODUKTY:
        abort(404)
    return f"Produkt: {PRODUKTY[id]}"

if __name__ == "__main__":
    app.run(debug=True)
