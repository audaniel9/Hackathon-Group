from flask import Blueprint, current_app, render_template,request, session, flash,request
from people.models.models import Users, Shelters



main = Blueprint('main',__name__)


@main.route('/',methods = ["GET"])
def index():
    return render_template('index.html')

@main.route('/login', methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        POST_USERNAME = str(request.form['username'])
        POST_PASSWORD = str(request.form['password'])

        if Users.query.filter_by(username=POST_USERNAME,password=POST_PASSWORD).first():
            return  render_template('index.html')
    else:
        return render_template('login.html')

    #else if request == 'GET'

@main.route("/logout")
def logout():
    session['logged_in'] = False
    return render_template('index.html')
