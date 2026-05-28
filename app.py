from cs50 import SQL
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
db = SQL("sqlite:///database.db")




@app.route("/")
def index():
    dieren = db.execute("SELECT * FROM DIEREN")
    categorieen = db.execute("SELECT * FROM CATEGORIEEN")
    return render_template("index.html", categorieen=categorieen, dieren=dieren)
@app.route("/Dieren")
def dieren():
    dieren = db.execute("SELECT naam FROM DIEREN")
    categorieen = db.execute("SELECT * FROM CATEGORIEEN")

    return render_template("Dieren.html", categorieen=categorieen, dieren=dieren)
@app.route("/Kaart")
def kaart():
    return render_template("kaart.html")

@app.route("/dier/<naam>")
def dierpagina(naam):
    resultaat = db.execute("SELECT * FROM DIEREN WHERE naam = ?", naam)
    if len(resultaat) == 0:
        return "Dier niet gevonden", 404
    return render_template("dierpagina.html", dier=resultaat[0])