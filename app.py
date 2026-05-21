#registratie website voor sporten

from cs50 import SQL
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
#maak arrays voor de verschillende categorieën dieren
CATEGORIEEN = ["Katachtigen", "Mensapen", "Beren", "Kleine roofdieren", "Zeedieren", "Hoefdieren", "Vogels", "Reptielen", "Aquariumdieren"]
KATACHTIGEN = ["Leeuw", "Amoertijger", "Jaguar", "Amoerluipaard"]
MENSAPEN = ["Gorilla", "Chimpansee", "Uilenkopmeerkat"]
BEREN = ["Brilbeer"]
KLEINE_ROOFDIEREN = ["Rode panda", "Stokstaartje", "Neusbeer", "Vosmangoest", "Wasbeer"]
ZEEDIEREN = ["Californische zeeleeuw", "Gewone zeehond"]
HOEFDIEREN = ["Giraffe", "Okapi", "Kaapse buffel", "Anoa", "Nijlpaard", "Olifant"]
VOGELS = ["Pinguïn", "Afrikaanse vogelsoorten"]
REPTIELEN = ["Krokodil", "Alligator", "Slang", "Hagedis"]
AQUARIUMDIEREN = ["Tripische rifvissen", "Koralen", "Zoet- en zoutwatervissen"]
#route voor de indexpagina met categorieën
@app.route("/")
def index():
    return render_template("index.html", categorieen=CATEGORIEEN, katachtigen=KATACHTIGEN, mensapen=MENSAPEN, beren=BEREN, kleine_roofdieren=KLEINE_ROOFDIEREN, zeedieren=ZEEDIEREN, hoefdieren=HOEFDIEREN , vogels=VOGELS, reptielen=REPTIELEN, aquariumdieren=AQUARIUMDIEREN)
#route voor verschillende categorieën 
#route voor katachtigen
@app.route("/Katachtigen")
def katachtigen():
    return render_template("Katachtigen.html", katachtigen=KATACHTIGEN)
#route voor mensapen
@app.route("/Mensapen")
def mensapen():
    return render_template("mensapen.html", mensapen=MENSAPEN)
@app.route("/Categorie")
def categorie():
    return render_template("Categorie.html")
@app.route("/Kaart")
def kaart():
    return render_template("Kaart.html")