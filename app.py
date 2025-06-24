from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

batchmates = ["Diya", "Rohan", "Simran", "Aryan", "Sneha", "Rahul", "Anjali"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/random")
def get_random_name():
    return jsonify({"name": random.choice(batchmates)})
