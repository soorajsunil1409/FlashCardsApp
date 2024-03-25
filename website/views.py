from flask import Blueprint, render_template, request, redirect
import os
import csv

views = Blueprint('views', __name__)


def get_images(typ=None, lang="en") -> dict:
    if type == None: return None

    path = os.path.join(os.getcwd(), "website", "static", "images", typ)
    dir_list = sorted(os.listdir(path))
    res = {}
    trans_words = []
    trans_file_path = ""

    if lang == "hin":
        trans_file_path = "./website/static/data/hindi.csv"
    elif lang == "tel":
        trans_file_path = "./website/static/data/telugu.csv"
    elif lang == "tam":
        trans_file_path = "./website/static/data/tamil.csv"
    elif lang == "mal":
        trans_file_path = "./website/static/data/malayalam.csv"

    with open(trans_file_path, "r") as file:
        reader = csv.reader(file)
        next(reader)
        
        if typ == "objects":
            trans_words = [i[0] for i in reader]
        elif typ == "food":
            trans_words = [i[1] for i in reader]
        elif typ == "animals":
            trans_words = [i[2] for i in reader]


    print("\n".join(i.split(".")[0] for i in dir_list))

    for file, trans_word in zip(dir_list, trans_words):
        file_path = os.path.join("/", "images", typ, file)
        word = file.split(".")[0].capitalize()

        # print(trans_word)
        res[word] = [trans_word, file_path]
        # res[word] = file_path


    return res

@views.route("/")
def index():
    return render_template("index.html")


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

