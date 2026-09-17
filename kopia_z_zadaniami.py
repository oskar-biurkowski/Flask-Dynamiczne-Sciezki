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

@app.route("/start")
def start():
    return redirect(url_for("index"))

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

@app.route("/czesc/<imie>/<int:wiek>")
def czesc_wiek(imie, wiek):
    return f"Cześć, {imie}, masz {wiek} lat!"

@app.route("/uzytkownik/<imie>/<nazwisko>")
def uzytkownik(imie, nazwisko):
    return f"Użytkownik: {imie} {nazwisko}"

@app.route("/dodaj/<int:a>/<int:b>")
def dodaj(a, b):
    return f"{a} + {b} = {a + b}"

@app.route("/odejmij/<int:a>/<int:b>")
def odejmij(a, b):
    return f"{a} - {b} = {a - b}"

@app.route("/pomnoz/<int:a>/<int:b>")
def pomnoz(a, b):
    return f"{a} * {b} = {a * b}"

@app.route("/podziel/<int:a>/<int:b>")
def podziel(a, b):
    if b == 0:
        return "Nie dzielimy przez zero", 400
    return f"{a} / {b} = {a / b}"

@app.route("/potega/<int:a>/<int:b>")
def potega(a, b):
    return f"{a} ^ {b} = {a ** b}"

@app.route("/tabliczka/<int:n>")
def tabliczka(n):
    if n < 1 or n > 20:
        return "Liczba musi być w przedziale od 1 do 20", 400
    wiersze = []
    for i in range (1,11):
        wiersze.append(f"{n} x {i} = {n * i}")
    return "<br>".join(wiersze)

        

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

@app.route("/element/<int:id>")
def element(id):
    if id not in PRODUKTY:
        abort(404)
    return f"Produkt: {PRODUKTY[id]}"

@app.route("/elementy")
def elementy():
    tekst = ""
    for id in PRODUKTY:
        tekst += f"{id}: {PRODUKTY[id]}<br>"
    return tekst

if __name__ == "__main__":
    app.run(debug=True)
