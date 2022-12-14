'''
Product: Website Hacktoberfest Project
Description: Flask app that runs index.html
Author: Benjamin Norman 2022
'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=80)
