from flask import Flask, render_template, jsonify
from data import QUESTIONS

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("game.html")

@app.route("/api/questions")
def questions():
    return jsonify(QUESTIONS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
