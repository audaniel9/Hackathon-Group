from flask import Blueprint, current_app, render_template,request, session, flash,request,redirect,url_for
from people.models.models import Users, Shelters,Jobs
import requests


main = Blueprint('main',__name__)


@main.route('/',methods = ["GET"])
def index():
    logged = str(request.form.get('username'))
    if logged:
        return redirect(url_for('main.login'))
    else:
        return render_template('index.html')

@main.route('/login', methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        POST_USERNAME = str(request.form['username'])
        POST_PASSWORD = str(request.form['password'])
        if Shelters.query.filter_by(username=POST_USERNAME,password=POST_PASSWORD).first():
            session['logged_in'] = True
            return  render_template('index.html',username=POST_USERNAME)

        elif Users.query.filter_by(username=POST_USERNAME,password=POST_PASSWORD).first():
            session['logged_in'] = True
            return  render_template('index.html',username=POST_USERNAME)
        else:
            return  render_template('login.html',error='invalid username or password')
    else:
        return render_template('login.html')

@main.route("/registration/shelter", methods = ['POST','GET'])
def registration():
    if request.method == 'POST':
        s_username = str(request.form['username'])
        s_psw = str(request.form['password'])
        s_email = str(request.form['email'])
        s_address = str(request.form['address'])
        s_city = str(request.form['city'])
        s_state = str(request.form['state'])
        s_zipcode = str(request.form['zip'])
        s_description = str(request.form['message'])


        if Shelters.query.filter_by(username = s_username).count() > 0:
            return render_template("shelterRegistration.html", error = "the username already exists please choose a UNIQUE one foo")

        if Shelters.query.filter_by(email_address = s_email).count() > 0:
            return render_template("shelterRegistration.html", error =  "the e-mail is already registered; you probably got hacked lel")

        else:
            shelter = Shelters(username = request.form['username'],email_address=request.form['email'],state=request.form['state']
                    ,zip_code=request.form['zipCode'],address=request.form['address'],city=request.form['city'],
                    password=request.form['password'])
            Shelters.query.add(shelter)
            Shelters.query.commit()
            return render_template('login.html')
    else:
        return render_template("shelterRegistration.html")



@main.route("/registration/volunteer", methods = ['POST','GET'])
def volunteer_registration():
    if request.method == 'GET':
        return render_template("volunteerRegistration.html")

    if request.method == 'POST':
        u_firstname = str(request.form['firstname'])
        u_lastname = str(request.form['lastname'])
        u_username = str(request.form['username'])
        u_psw = str(request.form['password'])
        u_email = str(request.form['email'])
        u_address = str(request.form['address'])
        u_city = str(request.form['city'])
        u_state = str(request.form['state'])
        u_zipcode = str(request.form['zip'])
        u_description = str(request.form['message'])

        fishlist = {u_firstname, u_lastname, u_username, u_psw, u_email, u_address, u_city, u_state, u_zipcode,
                    u_description}

        if len(u_firstname) == 0:
            return  'fail' #render_template("error.html")

        for item in fishlist:
            if len(item) == 0:
                return 'fail' #render_template("error.html")

        return render_template("index.html")

    # if db.query.filter(username == s_username):
    #    error = "the username already exists please choose a UNIQUE one foo"

    # if db.query(Product).filter(email_address == s_email):
    #    error = "the e-mail is already registered; you probably got hacked lel"

    # else:
# return redirect(url_for('where to redirect'))
@main.route('/jobs',methods = ['GET'])
def jobs():
    if Users.query.filter(username=request.form['username']).count() > 0:
        user = Users.query.filter(username=request.form['username'])

        for column in row.__table__.columns:
            if str(column.name) == 'state':
                state = str(getattr(row, column.name))
            if str(column.name) == 'city':
                city = str(getattr(row, column.name))

        jobs = {}
        shelters = Shelters.query.filter_by(city=city,state=states)

        for shelter_name in shelters:
            shelter_name = str(shelters.shelter_name)
            shelters_in_area[shelter_name] = [s.city,s.address,s.zip_code,s.state]

        closest_shelters[d.key()] = oscar(d.key())
        keylist = closest_shelters.keys()
        keylist.sort()

        finallist ={}
        for key in keylist:
        	finallist[closest_shelters[key]] = key
        ##get closest jobs
        return "sucess"
    else:
        return "failure"


@main.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('/'))
