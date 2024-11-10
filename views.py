from flask import Blueprint, jsonify,render_template, request,redirect,url_for

views = Blueprint(__name__,"views")

@views.route("/")
def home():
    return render_template("index.html",name="Tim")

@views.route("/profile/<username>")
def profile(username):
    args= request.args
    name=args.get('name')
    return render_template("index.html",name=username)


@views.route("/json")
def get_json():
    return jsonify({'name':'Tim','Coolness':10})

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@views.route("/go_to_home")

def go_to_home():
    return redirect (url_for("views.get_json"))

