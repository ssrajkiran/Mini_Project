from flask import Flask

from flask import render_template,request
app = Flask(__name__)

@app.errorhandler(404)
def not_found():
    return render_template("public/404.html")