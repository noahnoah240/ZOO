from cs50 import SQL
from flask import Flask, render_template, request, redirect, session, jsonify 
from werkzeug.security import check_password_hash, generate_password_hash #Zorgt ervoor dat wachtwoorden niet leesbaar zijn in de database.
import os

app = Flask(__name__) #maak variable "app" aan
app.config['SECRET_KEY'] = 'your-secret-key-change-this-in-production' 
db = SQL("sqlite:///database.db") #maakt verbinding met de database


def initialize_database(): #maakt tabellen voor gebruikers
    db.execute("CREATE TABLE IF NOT EXISTS USERS (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, password TEXT NOT NULL)")
    

initialize_database()

@app.route("/") #startpagina
def index():
    dieren = db.execute("SELECT * FROM DIEREN") 
    categorieen = db.execute("SELECT * FROM CATEGORIEEN")
    return render_template("index.html", categorieen=categorieen, dieren=dieren)
@app.route("/Dieren")
def dieren():
    dieren = db.execute("SELECT * FROM DIEREN")
    categorieen = db.execute("SELECT * FROM CATEGORIEEN")

    return render_template("Dieren.html", categorieen=categorieen, dieren=dieren)
@app.route("/Kaart")
def kaart():
    dieren = db.execute("SELECT * FROM DIEREN")
    return render_template("kaart.html", dieren=dieren)

@app.route("/dier/<naam>")
def dierpagina(naam):
    resultaat = db.execute("SELECT * FROM DIEREN WHERE naam = ?", naam)
    if len(resultaat) == 0:
        return "Dier niet gevonden", 404
       
    return render_template("dierpagina.html", dier=resultaat[0])

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        
        # Validation
        if not username:
            return render_template("register.html", error="Username is required")
        if not password:
            return render_template("register.html", error="Password is required")
        if password != confirmation:
            return render_template("register.html", error="Passwords do not match")
        
        # Check if username already exists
        existing = db.execute("SELECT * FROM USERS WHERE username = ?", username)
        if len(existing) > 0:
            return render_template("register.html", error="Username already exists")
        
        # Hash password and insert user
        hashed_password = generate_password_hash(password)
        db.execute("INSERT INTO USERS (username, password) VALUES (?, ?)", username, hashed_password)
        
        return redirect("/login")
    
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if not username or not password:
            return render_template("login.html", error="Username and password required")
        
        # Check user in database
        users = db.execute("SELECT * FROM USERS WHERE username = ?", username)
        if len(users) != 1 or not check_password_hash(users[0]["password"], password):
            return render_template("login.html", error="Invalid username or password")
        
        # Store user in session
        session["user_id"] = users[0]["id"]
        session["username"] = users[0]["username"]
        
        return redirect("/")
    
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/api/favorite", methods=["POST"])
def toggle_favorite():
    if "user_id" not in session:
        return jsonify({"error": "Not logged in"}), 401
    
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    dier_id = data.get("dier_id")
    try:
        dier_id = int(dier_id)
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid dier_id"}), 400
    
    user_id = session["user_id"]
    
    # Check if already favorited
    existing = db.execute(
        "SELECT * FROM FAVORIETEN WHERE user_id = ? AND dier_id = ?",
        user_id, dier_id
    )
    
    if len(existing) > 0:
        # Remove favorite (unfavorite)
        db.execute(
            "DELETE FROM FAVORIETEN WHERE user_id = ? AND dier_id = ?",
            user_id, dier_id
        )
        return jsonify({"favorited": False})
    else:
        # Check if user already has a favorite
        current_favorite = db.execute(
            "SELECT * FROM FAVORIETEN WHERE user_id = ?",
            user_id
        )
        
        if len(current_favorite) > 0:
            # Remove old favorite and add new one
            db.execute(
                "DELETE FROM FAVORIETEN WHERE user_id = ?",
                user_id
            )
        
        # Add new favorite
        db.execute(
            "INSERT INTO FAVORIETEN (user_id, dier_id) VALUES (?, ?)",
            user_id, dier_id
        )
        return jsonify({"favorited": True})

@app.route("/api/favorite_status/<int:dier_id>")
def favorite_status(dier_id):
    if "user_id" not in session:
        return jsonify({"favorited": False})
    
    favorite = db.execute(
        "SELECT * FROM FAVORIETEN WHERE user_id = ? AND dier_id = ?",
        session["user_id"], dier_id
    )
    return jsonify({"favorited": len(favorite) > 0})

if __name__ == "__main__":
    app.run(debug=True)