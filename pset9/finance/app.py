# key: export API_KEY=pk_12d0bde394314377a40b64c3fdc283e2

import os
import datetime
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # Assign user ID to a variable and use it to look up information
    user = session["user_id"]
    purchases = db.execute("SELECT symbol, price, SUM(shares) AS shares from purchases WHERE user_id = ?", user)

    user_balance = db.execute("SELECT cash FROM users WHERE id = :id", id=user)
    user_balance = user_balance[0]["cash"]

    return render_template("index.html", purchases=purchases, user_balance=user_balance)




@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    # GET route
    if request.method == "GET":
        return render_template("buy.html")

    # POST route
    elif request.method == "POST":
        symbol = request.form.get("symbol")
        symbol = symbol.upper()
        shares = request.form.get("shares")
        shares = int(shares)

        if shares == None or shares < 0:
            return apology("Please enter a positive number of shares")

        if symbol == None:
            return apology("Please enter a symbol")

        stock_info = lookup(symbol)

        if stock_info == None:
            return("Error")

        stock_price = stock_info["price"]

        price = shares * stock_price

        user = session["user_id"]

        # Check in db if user has enough cash to complete the purhcase
        user_balance = db.execute("SELECT cash FROM users WHERE id = :id", id=user)

        price = int(price)

        # Check if user has enough cash to make the purchase
        if user_balance[0]["cash"] < price:
            return apology("You have insufficient funds for this transaction")

        # Balance after making a purchase
        new_balance = user_balance[0]["cash"] - price

        current_time = datetime.datetime.now()

        # Update user and purchase tables
        db.execute("UPDATE users SET cash = ? WHERE id = ?", new_balance, user)

        db.execute("INSERT INTO purchases (user_id,symbol,price,date,shares) VALUES (?,?,?,?,?)",
                  user,symbol,price,current_time,shares)

        return("HEEEY HOW YOU DOIN?")


    # Block any other route
    else:
        return apology("An unexpected error has occurred")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # GET route
    if request.method == "GET":
        return render_template("quote.html")

    # POST route
    elif request.method == "POST":
        symbol = request.form.get("symbol")

        if not symbol:
            return apology("Please enter a valid symbol.")

        stock_info = lookup(symbol)

        if not stock_info:
            return apology("Stock price could not be found.")

        else:
            return render_template("quoted.html", symbol = stock_info["symbol"], name = stock_info["name"], price = stock_info["price"])

    # Block any other route
    else:
        return apology("An unknown error has occurred")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Accept GET and POST requests
    if request.method == "GET":
        return render_template("register.html")

    elif request.method == "POST":
        username = request.form.get("username")

        # Check if username is already in use
        username_check = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(username_check) == 1:
            return apology("This username is not available")

        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username or not password or not confirmation:
            return apology("Please fill in all fields")

        if password != confirmation:
            return apology("Please enter the same password twice")

        # Hashes password if credential details have been approved
        hashed_password = generate_password_hash(password)

        user = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hashed_password)

        # Start a session for the new user
        session["user_id"] = user

        return redirect("/")

    # Make sure only the GET and POST method are accepted
    else:
        return apology("An unknown error has occurred")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    if request.method == "GET":

        user = session["user_id"]

        current = db.execute("SELECT symbol FROM portfolio WHERE userid = :id",id=user)

        return render_template("sell.html", current=current)

    elif request.method == "POST":
        ...


    else:
        return apology("An unknown error has occurred")
