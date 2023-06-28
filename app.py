from flask import Flask, render_template

appw = Flask(__name__)

@appw.route("/")
def parte1() :
    return render_template("index.html")

appw.run()