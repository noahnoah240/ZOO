import sqlite3 
variable = sqlite3.connect('database.db')
cursor = variable.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS DIEREN (id INTEGER PRIMARY KEY AUTOINCREMENT, naam TEXT, beschrijving TEXT, categorie TEXT)")
cursor.execute("INSERT OR IGNORE INTO DIEREN (naam, beschrijving, categorie) VALUES ('Leeuw', 'De leeuw is een grote katachtige die in Afrika en delen van Azië voorkomt. Ze staan bekend om hun manen en worden vaak de \"koning van de jungle\" genoemd.', 'Katachtigen')")
cursor.execute("INSERT OR IGNORE INTO DIEREN (naam, beschrijving, categorie) VALUES ('Amoertijger', 'De amoertijger, ook wel Siberische tijger genoemd, is een van de grootste tijgersoorten en komt voor in de bossen van het Russische Verre Oosten. Ze hebben een dikke vacht om zich te beschermen tegen de koude winters.', 'Katachtigen')")
cursor.execute("INSERT OR IGNORE INTO DIEREN (naam, beschrijving, categorie) VALUES ('Jaguar', 'De jaguar is een grote katachtige die in de regenwouden van Midden- en Zuid-Amerika voorkomt. Ze staan bekend om hun gespierde bouw en krachtige kaken.', 'Katachtigen')")
cursor.execute("INSERT OR IGNORE INTO DIEREN (naam, beschrijving, categorie) VALUES ('Amoerluipaard', 'Het amoerluipaard, ook wel Siberische luipaard genoemd, is een zeldzame en bedreigde katachtige die voorkomt in de bossen van het Russische Verre Oosten. Ze hebben een dikke vacht en zijn uitstekend aangepast aan koude klimaten.', 'Katachtigen')")

cursor.execute("INSERT OR IGNORE INTO DIEREN (naam, beschrijving, categorie) VALUES ('Gorilla', 'De gorilla is een grote mensachtige die in de regenwouden van Afrika voorkomt. Ze staan bekend om hun kracht en sociale gedrag.', 'Mensapen')")
cursor.execute("INSERT OR IGNORE INTO DIEREN (naam, beschrijving, categorie) VALUES ('Chimpansee', 'De chimpansee is een mensachtige die in de bossen van Afrika voorkomt. Ze zijn nauw verwant aan mensen en staan bekend om hun intelligentie en sociale structuren.', 'Mensapen')")
cursor.execute("INSERT OR IGNORE INTO DIEREN (naam, beschrijving, categorie) VALUES ('Uilenkopmeerkat', 'De uilenkopmeerkat is een kleine mensachtige die in de droge gebieden van Afrika voorkomt. Ze hebben een uniek uiterlijk met een ronde kop en grote ogen, waardoor ze lijken op een uil.', 'Mensapen')")

cursor.execute("INSERT OR IGNORE INTO DIEREN (naam, beschrijving, categorie) VALUES ('Brilbeer', 'De brilbeer is een middelgrote beer die voorkomt in de Andes van Zuid-Amerika. Ze staan bekend om de witte vlekken rond hun ogen, die lijken op een bril.', 'Beren')")

cursor.execute("INSERT OR IGNORE INTO DIEREN (naam, beschrijving, categorie) VALUES ('Rode panda', 'De rode panda is een kleine zoogdier die voorkomt in de bergachtige gebieden van Nepal, India, Bhutan en China. Ze hebben een roodbruine vacht en een lange, pluizige staart.', 'Kleine_Roofdieren')")
cursor.execute("INSERT OR IGNORE INTO DIEREN (naam, beschrijving, categorie) VALUES ('Stokstaartje', 'Het stokstaartje is een kleine zoogdier die voorkomt in de droge gebieden van Afrika. Ze staan bekend om hun sociale gedrag en het feit dat ze vaak rechtop staan om hun omgeving in de gaten te houden.', 'Kleine_Roofdieren')")
cursor.execute("INSERT OR IGNORE INTO DIEREN (naam, beschrijving, categorie) VALUES ('Neusbeer', 'De neusbeer is een kleine zoogdier die voorkomt in de bossen van Midden- en Zuid-Amerika. Ze hebben een lange snuit en een dikke vacht, en staan bekend om hun nieuwsgierige aard.', 'Kleine_Roofdieren')")
cursor.execute("INSERT OR IGNORE INTO DIEREN (naam, beschrijving, categorie) VALUES ('Vosmangoest', 'De vosmangoest is een kleine zoogdier die voorkomt in de droge gebieden van Afrika. Ze hebben een roodbruine vacht en staan bekend om hun behendigheid en snelheid.', 'Kleine_Roofdieren')")
cursor.execute("INSERT OR IGNORE INTO DIEREN (naam, beschrijving, categorie) VALUES ('Wasbeer', 'De wasbeer is een kleine zoogdier die voorkomt in Noord- en Zuid-Amerika. Ze hebben een grijze vacht en een kenmerkende zwarte \"masker\" rond hun ogen.', 'Kleine_Roofdieren')")

cursor.execute("INSERT OR IGNORE INTO DIEREN (naam, beschrijving, categorie) VALUES ('Californische zeeleeuw', 'De Californische zeeleeuw is een zeezoogdier dat voorkomt langs de westkust van Noord-Amerika. Ze staan bekend om hun speelse gedrag en worden vaak gezien in dierentuinen en aquaria.', 'Zeedieren')")
cursor.execute("INSERT OR IGNORE INTO DIEREN (naam, beschrijving, categorie) VALUES ('Gewone zeehond', 'De gewone zeehond is een zeezoogdier dat voorkomt in de kustwateren van Europa, Noord-Amerika en delen van Azië. Ze hebben een grijze vacht en staan bekend om hun vermogen om zowel op het land als in het water te leven.', 'Zeedieren')")

cursor.execute("INSERT OR IGNORE INTO DIEREN (naam, beschrijving, categorie) VALUES ('Giraffe', 'De giraffe is een grote hoefdier die voorkomt in de savannes van Afrika. Ze staan bekend om hun lange nek en benen, en hun unieke vlekkenpatroon.', 'Hoefdieren')")
cursor.execute("INSERT OR IGNORE INTO DIEREN (naam, beschrijving, categorie) VALUES ('Okapi', 'De okapi is een middelgrote hoefdier die voorkomt in de regenwouden van Congo. Ze hebben een uniek uiterlijk met een lange nek en strepen op hun benen, waardoor ze lijken op een kruising tussen een giraffe en een zebra.', 'Hoefdieren')")
cursor.execute("INSERT OR IGNORE INTO DIEREN (naam, beschrijving, categorie) VALUES ('Kaapse buffel', 'De Kaapse buffel is een grote hoefdier die voorkomt in de savannes van Afrika. Ze staan bekend om hun kracht en agressieve gedrag, en worden vaak beschouwd als een van de gevaarlijkste dieren in Afrika.', 'Hoefdieren')")
cursor.execute("INSERT OR IGNORE INTO DIEREN (naam, beschrijving, categorie) VALUES ('Anoa', 'De anoa is een kleine hoefdier die voorkomt in de regenwouden van Indonesië. Ze hebben een gedrongen lichaam en korte poten, en staan bekend om hun schuwe aard.', 'Hoefdieren')")
cursor.execute("INSERT OR IGNORE INTO DIEREN (naam, beschrijving, categorie) VALUES ('Nijlpaard', 'De nijlpaard is een grote hoefdier die voorkomt in de rivieren en meren van Afrika. Ze staan bekend om hun enorme omvang en agressieve gedrag, en worden vaak beschouwd als een van de gevaarlijkste dieren in Afrika.', 'Hoefdieren')")
cursor.execute("INSERT OR IGNORE INTO DIEREN (naam, beschrijving, categorie) VALUES ('Olifant', 'De olifant is een grote hoefdier die voorkomt in Afrika en delen van Azië. Ze staan bekend om hun enorme omvang, lange slurf en grote oren, en worden vaak beschouwd als een van de meest intelligente dieren op aarde.', 'Hoefdieren')")

cursor.execute("INSERT OR IGNORE INTO DIEREN (naam, beschrijving, categorie) VALUES ('Pinguïn', 'De pinguïn is een vogel die voorkomt in het zuidelijk halfrond, vooral in Antarctica. Ze staan bekend om hun zwart-witte verenkleed en hun vermogen om te zwemmen.', 'Vogels')")
cursor.execute("INSERT OR IGNORE INTO DIEREN (naam, beschrijving, categorie) VALUES ('Afrikaanse vogelsoorten', 'Afrika herbergt een enorme diversiteit aan vogelsoorten, waaronder kleurrijke papegaaien, majestueuze arenden en sierlijke flamingos. Deze vogels spelen een belangrijke rol in de ecosystemen van Afrika.', 'Vogels')")

cursor.execute("INSERT OR IGNORE INTO DIEREN (naam, beschrijving, categorie) VALUES ('Krokodil', 'De krokodil is een grote reptiel die voorkomt in de tropische gebieden van Afrika, Azië, Amerika en Australië. Ze staan bekend om hun krachtige kaken en hun vermogen om zowel op het land als in het water te leven.', 'Reptielen')")
cursor.execute("INSERT OR IGNORE INTO DIEREN (naam, beschrijving, categorie) VALUES ('Alligator', 'De alligator is een grote reptiel die voorkomt in de zuidelijke Verenigde Staten en China. Ze lijken op krokodillen, maar hebben een bredere snuit en zijn over het algemeen minder agressief.', 'Reptielen')")
cursor.execute("INSERT OR IGNORE INTO DIEREN (naam, beschrijving, categorie) VALUES ('Slangen', 'Slangen zijn een diverse groep reptielen die voorkomen in bijna alle delen van de wereld, behalve Antarctica. Ze variëren in grootte van kleine, onschuldige soorten tot grote, gevaarlijke soorten zoals de anaconda en de zwarte mamba.', 'Reptielen')")
cursor.execute("INSERT OR IGNORE INTO DIEREN (naam, beschrijving, categorie) VALUES ('Hagedis', 'Hagedissen zijn een diverse groep reptielen die voorkomen in bijna alle delen van de wereld. Ze variëren in grootte van kleine, onschuldige soorten tot grote, indrukwekkende soorten zoals de Komodovaraan.', 'Reptielen')")

cursor.execute("INSERT OR IGNORE INTO DIEREN (naam, beschrijving, categorie) VALUES ('Tropische rifvissen', 'Tropische rifvissen zijn een diverse groep vissen die voorkomen in de warme, ondiepe wateren van tropische koraalriffen over de hele wereld. Ze staan bekend om hun felle kleuren en unieke patronen.', 'Aquariumdieren')")
cursor.execute("INSERT OR IGNORE INTO DIEREN (naam, beschrijving, categorie) VALUES ('Koralen', 'Koralen zijn mariene ongewervelde dieren die voorkomen in de warme, ondiepe wateren van tropische koraalriffen over de hele wereld. Ze vormen de structuur van koraalriffen en bieden onderdak aan een enorme diversiteit aan marien leven.', 'Aquariumdieren')")
cursor.execute("INSERT OR IGNORE INTO DIEREN (naam, beschrijving, categorie) VALUES ('Zoet- en zoutwatervissen', 'Zoet- en zoutwatervissen zijn een diverse groep vissen die voorkomen in zowel zoetwater- als zoutwateromgevingen over de hele wereld. Ze variëren in grootte van kleine, onschuldige soorten tot grote, indrukwekkende soorten zoals de meerval en de haai.', 'Aquariumdieren')")

cursor.execute("CREATE TABLE IF NOT EXISTS CATEGORIEEN (id INTEGER PRIMARY KEY AUTOINCREMENT, naam TEXT)")
cursor.execute("INSERT OR IGNORE INTO CATEGORIEEN (naam) VALUES ('Katachtigen')")
cursor.execute("INSERT OR IGNORE INTO CATEGORIEEN (naam) VALUES ('Mensapen')")
cursor.execute("INSERT OR IGNORE INTO CATEGORIEEN (naam) VALUES ('Beren')")
cursor.execute("INSERT OR IGNORE INTO CATEGORIEEN (naam) VALUES ('Kleine_Roofdieren')")
cursor.execute("INSERT OR IGNORE INTO CATEGORIEEN (naam) VALUES ('Zeedieren')")
cursor.execute("INSERT OR IGNORE INTO CATEGORIEEN (naam) VALUES ('Hoefdieren')")
cursor.execute("INSERT OR IGNORE INTO CATEGORIEEN (naam) VALUES ('Vogels')")
cursor.execute("INSERT OR IGNORE INTO CATEGORIEEN (naam) VALUES ('Reptielen')")
cursor.execute("INSERT OR IGNORE INTO CATEGORIEEN (naam) VALUES ('Aquariumdieren')")

cursor.execute("SELECT * FROM DIEREN JOIN CATEGORIEEN ON CATEGORIEEN.naam = DIEREN.categorie")
variable.commit()
variable.close()