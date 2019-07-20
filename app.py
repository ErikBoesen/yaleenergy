from flask import Flask, render_template
import os
import yalebuildings
import yaleenergydata

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")
