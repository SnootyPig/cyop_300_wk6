"""Flask app with three routes and dynamic date rendering."""
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "bubblesBestKey"

users = {}

@app.route("/")
def home() -> str:
    """Home page."""
    my_time = datetime.now()
    return render_template("index.html", my_time=my_time)

@app.route("/grand")
def grand() -> str:
    """Page 2."""
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("grand.html")

@app.route("/moregrand")
def moregrand() -> str:
    """Page 3."""
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("moregrand.html")

@app.route("/register", methods=["GET", "POST"])
def register() -> str:
    """User registration."""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users:
            return "Username already exists!"
        users[username] = password
        return redirect(url_for("login"))
    return render_template("reg.html")

@app.route("/login", methods=["GET", "POST"])
def login() -> str:
    """User login."""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.get(username) == password:
            session["logged_in"] = True
            return redirect(url_for("home"))
        return "Egads! Invalid credentials!"
    return render_template("login.html")

if __name__ == "__main__":
    app.run()
