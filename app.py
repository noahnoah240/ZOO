from cs50 import SQL
from flask import Flask, render_template, request, redirect, session, jsonify 
from werkzeug.security import check_password_hash, generate_password_hash #Zorgt ervoor dat wachtwoorden niet leesbaar zijn in de database.
import os

app = Flask(__name__) #maak variable "app" aan
app.config['SECRET_KEY'] = 'your-secret-key-change-this-in-production' 
db = SQL("sqlite:///database.db") #maakt verbinding met de database
db.execute("PRAGMA foreign_keys = ON")


def initialize_database(): #maakt tabellen voor gebruikers
    db.execute("CREATE TABLE IF NOT EXISTS USERS (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, password TEXT NOT NULL)")
    db.execute("""CREATE TABLE IF NOT EXISTS REVIEWS (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        dier_id INTEGER NOT NULL,
        review TEXT NOT NULL,
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES USERS(id),
        FOREIGN KEY (dier_id) REFERENCES DIEREN(id),
        UNIQUE(user_id, dier_id)
    )""")
    db.execute("""CREATE TABLE IF NOT EXISTS PARK_REVIEWS (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        review TEXT NOT NULL,
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES USERS(id)
    )""")

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
    return render_template("Kaart.html", dieren=dieren)

@app.route("/admin")
def admin():
    if session.get('username') != 'Noah.M':
        return redirect("/login")

    animal_reviews = db.execute(
        "SELECT REVIEWS.id AS review_id, REVIEWS.review, REVIEWS.created_at, USERS.username, DIEREN.naam AS dier_naam "
        "FROM REVIEWS "
        "JOIN USERS ON REVIEWS.user_id = USERS.id "
        "JOIN DIEREN ON REVIEWS.dier_id = DIEREN.id "
        "ORDER BY USERS.username ASC, REVIEWS.created_at DESC"
    )

    park_reviews = db.execute(
        "SELECT PARK_REVIEWS.id AS review_id, PARK_REVIEWS.review, PARK_REVIEWS.created_at, USERS.username "
        "FROM PARK_REVIEWS "
        "JOIN USERS ON PARK_REVIEWS.user_id = USERS.id "
        "ORDER BY USERS.username ASC, PARK_REVIEWS.created_at DESC"
    )

    users = db.execute("SELECT id, username FROM USERS ORDER BY username ASC")

    return render_template("admin.html", animal_reviews=animal_reviews, park_reviews=park_reviews, users=users)

@app.route("/reviews", methods=["GET", "POST"])
def reviews():
    error = None

    if request.method == "POST":
        if "user_id" not in session:
            return redirect("/login")

        review_text = request.form.get("review")
        if not review_text or not review_text.strip():
            error = "Review is verplicht"
        else:
            review_text = review_text.strip()
            db.execute(
                "INSERT INTO PARK_REVIEWS (user_id, review, created_at) VALUES (?, ?, datetime('now'))",
                session["user_id"], review_text
            )
            return redirect("/reviews")

    animal_reviews = db.execute(
        "SELECT REVIEWS.id AS review_id, REVIEWS.review, REVIEWS.created_at, REVIEWS.user_id, USERS.username, DIEREN.naam AS dier_naam "
        "FROM REVIEWS "
        "JOIN USERS ON REVIEWS.user_id = USERS.id "
        "JOIN DIEREN ON REVIEWS.dier_id = DIEREN.id "
        "ORDER BY REVIEWS.created_at DESC"
    )

    park_reviews = db.execute(
        "SELECT PARK_REVIEWS.id AS review_id, PARK_REVIEWS.review, PARK_REVIEWS.created_at, PARK_REVIEWS.user_id, USERS.username "
        "FROM PARK_REVIEWS "
        "JOIN USERS ON PARK_REVIEWS.user_id = USERS.id "
        "ORDER BY PARK_REVIEWS.created_at DESC"
    )

    return render_template("reviews.html", animal_reviews=animal_reviews, park_reviews=park_reviews, error=error)

@app.route("/dier/<naam>", methods=["GET", "POST"])
def dierpagina(naam):
    resultaat = db.execute("SELECT * FROM DIEREN WHERE naam = ?", naam)
    if len(resultaat) == 0:
        return "Dier niet gevonden", 404

    dier = resultaat[0]
    error = None

    if request.method == "POST":
        if "user_id" not in session:
            return redirect("/login")

        review_text = request.form.get("review")
        if not review_text or not review_text.strip():
            error = "Review is verplicht"
        else:
            review_text = review_text.strip()
            existing = db.execute(
                "SELECT * FROM REVIEWS WHERE user_id = ? AND dier_id = ?",
                session["user_id"], dier["id"]
            )
            if len(existing) > 0:
                db.execute(
                    "UPDATE REVIEWS SET review = ?, created_at = datetime('now') WHERE user_id = ? AND dier_id = ?",
                    review_text, session["user_id"], dier["id"]
                )
            else:
                db.execute(
                    "INSERT INTO REVIEWS (user_id, dier_id, review, created_at) VALUES (?, ?, ?, datetime('now'))",
                    session["user_id"], dier["id"], review_text
                )
            return redirect(f"/dier/{naam}")

    reviews = db.execute(
        "SELECT REVIEWS.id, REVIEWS.review, REVIEWS.created_at, REVIEWS.user_id, USERS.username FROM REVIEWS JOIN USERS ON REVIEWS.user_id = USERS.id WHERE REVIEWS.dier_id = ? ORDER BY REVIEWS.created_at DESC",
        dier["id"]
    )

    return render_template("dierpagina.html", dier=dier, reviews=reviews, error=error)

@app.route("/dier/<naam>/review/delete", methods=["POST"])
def delete_review(naam):
    if "user_id" not in session:
        return redirect("/login")

    review_id = request.form.get("review_id")
    if not review_id:
        return redirect(f"/dier/{naam}")

    try:
        review_id = int(review_id)
    except ValueError:
        return redirect(f"/dier/{naam}")

    review = db.execute("SELECT * FROM REVIEWS WHERE id = ?", review_id)
    if len(review) == 0 or (review[0]["user_id"] != session["user_id"] and session.get('username') != 'Noah.M'):
        return redirect(f"/dier/{naam}")

    db.execute("DELETE FROM REVIEWS WHERE id = ?", review_id)
    return redirect(f"/dier/{naam}")

@app.route("/reviews/park/delete", methods=["POST"])
def delete_park_review():
    if "user_id" not in session:
        return redirect("/login")

    review_id = request.form.get("review_id")
    if not review_id:
        return redirect("/reviews")

    try:
        review_id = int(review_id)
    except ValueError:
        return redirect("/reviews")

    review = db.execute("SELECT * FROM PARK_REVIEWS WHERE id = ?", review_id)
    if len(review) == 0 or (review[0]["user_id"] != session["user_id"] and session.get('username') != 'Noah.M'):
        return redirect("/reviews")

    db.execute("DELETE FROM PARK_REVIEWS WHERE id = ?", review_id)
    return redirect("/reviews")

@app.route("/reviews/animal/delete", methods=["POST"])
def delete_animal_review():
    if "user_id" not in session:
        return redirect("/login")

    review_id = request.form.get("review_id")
    if not review_id:
        return redirect("/reviews")

    try:
        review_id = int(review_id)
    except ValueError:
        return redirect("/reviews")

    review = db.execute("SELECT * FROM REVIEWS WHERE id = ?", review_id)
    if len(review) == 0 or (review[0]["user_id"] != session["user_id"] and session.get('username') != 'Noah.M'):
        return redirect("/reviews")

    db.execute("DELETE FROM REVIEWS WHERE id = ?", review_id)
    return redirect("/reviews")

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


@app.route("/admin/delete_user", methods=["POST"])
def admin_delete_user():
    if session.get('username') != 'Noah.M' or 'user_id' not in session:
        return redirect('/login')

    user_id = request.form.get('user_id')
    if not user_id:
        return redirect('/admin')

    try:
        user_id = int(user_id)
    except ValueError:
        return redirect('/admin')

    # Prevent admin from deleting their own account
    if user_id == session.get('user_id'):
        return redirect('/admin')

    # Remove user's reviews first, then the user
    db.execute("DELETE FROM REVIEWS WHERE user_id = ?", user_id)
    db.execute("DELETE FROM PARK_REVIEWS WHERE user_id = ?", user_id)
    db.execute("DELETE FROM USERS WHERE id = ?", user_id)

    return redirect('/admin')

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
if __name__ == "__main__":
    app.run(debug=True)