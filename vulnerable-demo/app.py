import os
from flask import Flask, session, redirect, url_for

app = Flask(__name__)

app.secret_key = os.environ.get("FLASK_SECRET_KEY")

if not app.secret_key:
    raise RuntimeError("Set the FLASK_SECRET_KEY environment variable.")

app.config["SESSION_COOKIE_NAME"] = "idor_vulnerable_session"

# Fictional accounts for controlled security testing
users = {
    1: {"name": "Alice", "email": "alice@example.test"},
    2: {"name": "Bob", "email": "bob@example.test"},
}

@app.route("/")
def home():
    return """
    <h1>Intentional IDOR Vulnerability Demonstration</h1>
    <p><a href="/login/1">Log in as Alice</a></p>
    <p><a href="/login/2">Log in as Bob</a></p>
    """

@app.route("/login/<int:user_id>")
def login(user_id):
    if user_id not in users:
        return "User not found", 404

    session.clear()
    session["user_id"] = user_id
    return redirect(url_for("profile", user_id=user_id))

@app.route("/profile/<int:user_id>")
def profile(user_id):
    logged_in_user_id = session.get("user_id")

    # Authentication check exists.
    if logged_in_user_id is None:
        return "Please log in first.", 401

    user = users.get(user_id)

    if user is None:
        return "User not found.", 404

    # INTENTIONAL IDOR VULNERABILITY:
    # The application does not check whether the logged-in
    # user is authorized to access the requested profile.

    return f"""
    <h1>Profile</h1>
    <p>Logged-in user ID: {logged_in_user_id}</p>
    <p>Profile owner: {user["name"]}</p>
    <p>Email: {user["email"]}</p>
    """

if __name__ == "__main__":
    # Keep this demonstration restricted to the local machine.
    app.run(host="127.0.0.1", port=5001, debug=False)
