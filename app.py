from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/suomi/")
@app.route("/suomi/<query>")
def serve_suomi(query=None):
    return render_template("map_suomi.html.jinja", query=query)

@app.route("/helsinki/")
@app.route("/helsinki/<query>")
def serve_helsinki(query=None):
    return render_template("map_helsinki.html.jinja", query=query)