from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Strona główna"

@app.route("/o-nas")
def o_nas():
    return "Jesteśmy klasą 4 Technik Programista. Robimy Sklep."

@app.route("/kontakt")
def kontakt():
    return "Napisz: sklep@symplelx.com"

@app.route("/regulamin")
def regulamin():
    return "Na tą chwilę, regulamin jeszcze nie powstał."

@app.route("/admin")
def tajne():
    return "Brak dostępu", 403

@app.route("/api/info")
def status():
    return {"nazwa": "Sklep internetowy", "autor": "Oskar Biurkowski", "wersja": "0.1"}

if __name__ == "__main__":
    app.run(debug=True)