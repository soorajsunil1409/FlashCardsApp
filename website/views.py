from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route("/")
def index():
    return render_template("index.html")

@views.route("/learn/hindi")
def learn_hindi():
    return render_template("hindi.html")

@views.route("/learn/malayalam")
def learn_malayalam():
    return render_template("malayalam.html")

@views.route("/learn/tamil")
def learn_tamil():
    return render_template("tamil.html")

@views.route("/learn/telugu")
def learn_telugu():
    return render_template("telugu.html")