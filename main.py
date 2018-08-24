
from flask import Flask , render_template, request, jsonify
import Uni_To_Zg
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    myinput = request.form['myinput']
    myinput = Uni_To_Zg.convert(myinput)
    output = myinput
    if myinput:
        return jsonify({'output': output})
    return jsonify({'output': "Plz write or paste text in input textarea"})

@app.route("/unitowin")
def unitowin():
    return render_template("unitowin.html")

@app.route("/wintouni")
def wintouni():
    return render_template("wintouni.html")

@app.route("/wintozawgyi")
def wintozawgyi():
    return render_template("wintozawgyi.html")

@app.route("/zawgyitouni")
def zawgyitouni():
    return render_template("zawgyitouni.html")

@app.route("/zawgyitowin")
def zawgyitowin():
    return render_template("zawgyitowin.html")

@app.route("/firstpages")
def firstpage():
    return render_template("firstpage.html")

if __name__ == "__main__":
    app.run(debug=True)
