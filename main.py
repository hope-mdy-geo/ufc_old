
from flask import Flask , render_template, request, jsonify
import Uni_To_Zg
import Zg_To_Uni
import Win_To_Uni
import Uni_To_Win
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

@app.route("/zawgyitouni")
def zawgyitouni():
    return render_template("zawgyitouni.html")

@app.route("/convert1", methods=["POST"])
def convert1():
    myinput = request.form['myinput']
    myinput = Zg_To_Uni.convert(myinput)
    output = myinput
    if myinput:
        return jsonify({'output': output})
    return jsonify({'output': "Plz write or paste text in input textarea"})

@app.route("/wintouni")
def wintouni():
    return render_template("wintouni.html")

@app.route("/convert2", methods=["POST"])
def convert2():
    myinput = request.form['myinput']
    myinput = Win_To_Uni.convert(myinput)
    output = myinput
    if myinput:
        return jsonify({'output': output})
    return jsonify({'output': "Plz write or paste text in input textarea"})

@app.route("/unitowin")
def unitowin():
    return render_template("unitowin.html")

@app.route("/convert3", methods=["POST"])
def convert3():
    myinput = request.form['myinput']
    myinput = Uni_To_Win.convert(myinput)
    output = myinput
    if myinput:
        return jsonify({'output': output})
    return jsonify({'output': "Plz write or paste text in input textarea"})


@app.route("/wintozawgyi")
def wintozawgyi():
    return render_template("wintozawgyi.html")

@app.route("/convert4", methods=["POST"])
def convert4():
    myinput = request.form['myinput']
    myinput = Win_To_Uni.convert(myinput)
    myinput = Uni_To_Zg.convert(myinput)
    output = myinput
    if myinput:
        return jsonify({'output': output})
    return jsonify({'output': "Plz write or paste text in input textarea"})

@app.route("/zawgyitowin")
def zawgyitowin():
    return render_template("zawgyitowin.html")

@app.route("/convert5", methods=["POST"])
def convert5():
    myinput = request.form['myinput']
    myinput = Zg_To_Uni.convert(myinput)
    myinput = Uni_To_Win.convert(myinput)
    output = myinput
    if myinput:
        return jsonify({'output': output})
    return jsonify({'output': "Plz write or paste text in input textarea"})

@app.route("/firstpages")
def firstpage():
    return render_template("firstpage.html")

if __name__ == "__main__":
    app.run(debug=True)
