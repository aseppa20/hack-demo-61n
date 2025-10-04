from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("page.html")

@app.route("/suomi/")
@app.route("/suomi/<query>")
def serve_suomi(query=None):
    return render_template("map_suomi.html.jinja", query=query)

@app.route("/helsinki/")
@app.route("/helsinki/<query>")
def serve_helsinki(query=None):
    return render_template("map_helsinki.html.jinja", query=query)


@app.route("/viesti/")
@app.route("/viesti/<query>")
def serve_viesti(query=None):
    return render_template("viesti.html", query = query)

if __name__ == "__main__":
    app.run(debug=True)