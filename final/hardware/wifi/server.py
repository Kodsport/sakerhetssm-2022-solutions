#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return '<a href="/flag">Press me for flag!</a>'

@app.route("/flag")
def flag():
    return 'SSM{fr33_w1f1_bu7_n0_fr33_1n73rn37_:(}'

app.run("0.0.0.0", 80)
