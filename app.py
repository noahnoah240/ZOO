#registratie website voor sporten

from cs50 import SQL
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
#maak arrays voor de verschillende categorieën dieren
CATEGORIEEN = ["Katachtigen", "Mensapen", "Beren", "Roofdieren", "Zeedieren", "Hoefdieren", "Vogels", "Reptielen", "Aquariumdieren"]
KATACHTIGEN = ["Leeuw", "Amoertijger", "Jaguar", "Amoerluipaard"]
MENSAPEN = ["Gorilla", "Chimpansee", "Uilenkopmeerkat"]
BEREN = ["Brilbeer"]
ROOFDIEREN = ["Rode panda", "Stokstaartje", "Neusbeer", "Vosmangoest", "Wasbeer"]
ZEEDIEREN = ["Californische zeeleeuw", "Gewone zeehond"]
HOEFDIEREN = ["Giraffe", "Okapi", "Kaapse buffel", "Anoa", "Nijlpaard", "Olifant"]
VOGELS = ["Pinguïn", "Afrikaanse vogelsoorten"]
REPTIELEN = ["Krokodil", "Alligator", "Slang", "Hagedis"]
AQUARIUMDIEREN = ["Tripische rifvissen", "Koralen", "Zoet- en zoutwatervissen"]
#route van startpagina
@app.route("/")
def index():
    return render_template("index.html", categorieen=CATEGORIEEN, katachtigen=KATACHTIGEN, mensapen=MENSAPEN, beren=BEREN, roofdieren=ROOFDIEREN, zeedieren=ZEEDIEREN, hoefdieren=HOEFDIEREN , vogels=VOGELS, reptielen=REPTIELEN, aquariumdieren=AQUARIUMDIEREN)
#route van pagina met dieren
@app.route("/Dieren")
def dieren():
    return render_template("Dieren.html")
#route van pagina met kaart
@app.route("/Kaart")
def kaart():
    return render_template("Kaart.html")
#route van elke pagina van elk individueel dier
for categorie in CATEGORIEEN: #loop door elke categorie heen
    for dier in eval(categorie.upper()): #loop door elk dier in de categorie heen
        def dierpagina(d=dier): 
            return render_template("dierpagina.html", dier=d)
        
        dierpagina.__name__ = f"dierpagina_{dier}"
        app.add_url_rule(f"/{dier}", endpoint=dier, view_func=dierpagina)