from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)


@views.route("/")
def index():
    return render_template("index.html")

@views.route("/learn", methods=["POST", "GET"])
def learn():
    if request.method == 'POST':
        res = request.form

        language = res["lang"]
        learn_type = res["button"]

        print(language, learn_type)
        
    return render_template("learn.html")