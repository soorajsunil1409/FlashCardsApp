from flask import Blueprint, render_template, request, redirect
import os
import csv
import pandas as pd

views = Blueprint('views', __name__)


##########################################
# Function to get images from the folder #
##########################################
def get_images(typ=None, lang="en") -> dict:
    if type == None: return None

    path = os.path.join(os.getcwd(), "website", "static", "images", typ)
    dir_list = sorted(os.listdir(path))
    res = {}
    trans_words = []
    trans_file_path = ""

    if lang == "hin":
        os.path.join(".", "website", "static", "data", "hindi.csv")
        trans_file_path = os.path.join(".", "website", "static", "data", "hindi.csv")
    elif lang == "tel":
        trans_file_path = os.path.join(".", "website", "static", "data", "telugu.csv")
    elif lang == "tam":
        trans_file_path = os.path.join(".", "website", "static", "data", "tamil.csv")
    elif lang == "mal":
        trans_file_path = os.path.join(".", "website", "static", "data", "malayalam.csv")
        
    file = pd.read_csv(trans_file_path, encoding="utf-8")
    print()
        
    if typ == "objects":
        trans_words = file["Object"].to_list()
    elif typ == "food":
        trans_words = file["Food"].to_list()
    elif typ == "animals":
        trans_words = file["Animal"].to_list()


    print("\n".join(i.split(".")[0] for i in dir_list))

    for file, trans_word in zip(dir_list, trans_words):
        file_path = f"/images/{typ}/{file}"
        word = file.split(".")[0].capitalize()

        res[word] = [trans_word, file_path]


    return res



#######################
# Route to index page #
#######################
@views.route("/")
def index():
    return render_template("index.html")



#######################
# Route to learn page #
#######################
@views.route("/learn", methods=["POST", "GET"])
def learn():
    result = {}

    if request.method == 'POST':
        res = request.form

        language = res["lang"]
        learn_type = res["button"]


        if language == "Hindi": language = "hin"
        elif language == "Telugu": language = "tel"
        elif language == "Tamil": language = "tam"
        elif language == "Malayalam": language = "mal"

        
        print(language, learn_type)

        result = get_images(learn_type, lang=language)
        return render_template("learn.html", result=result)
    else:
        return redirect("/")

