from flask import Flask, render_template, request, redirect, url_for, jsonify
from db import init_db, add_comment, get_comments, delete_comment
import time

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/add_comment", methods=["POST"])
def add_comment_route():
    username = request.form.get("username")
    content = request.form.get("content")
    if username and content:
        add_comment(username, content)
    return "", 204


@app.route("/get_comments", methods=["GET"])
def get_comments_route():
    comments = get_comments()
    return jsonify(comments)

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        password = request.form.get("password")
        if password == "Nazarka":
            comment_id = request.form.get("comment_id")
            if comment_id:
                delete_comment(comment_id)
        else:
            return "Невірний пароль!", 403
    comments = get_comments()
    return render_template("admin.html", comments=comments)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)