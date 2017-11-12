from flask import Flask, request, flash, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

#from your_app import name_of_db

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template("login.html")

@app.route("/registration/shelter", methods = ['POST','GET'])
def registration():
    if request.method == 'GET':
        return render_template("shelterRegistration.html")

    if request.method == 'POST':
        s_username = str(request.form['username'])
        s_psw = str(request.form['password'])
        s_email = str(request.form['email'])
        s_address = str(request.form['address'])
        s_city = str(request.form['city'])
        s_state = str(request.form['state'])
        s_zipcode = str(request.form['zip'])
        s_description = str(request.form['message'])

        return render_template("index.html")

        # if db.query.filter(username == s_username):
        #    error = "the username already exists please choose a UNIQUE one foo"

        # if db.query(Product).filter(email_address == s_email):
        #    error = "the e-mail is already registered; you probably got hacked lel"

        # else:
        #    return redirect(url_for('where to redirect'))


@app.route("/registration/volunteer", methods = ['POST','GET'])
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
        u_description = str(request.form['submitform'])

        fishlist = {u_firstname, u_lastname, u_username, u_psw, u_email, u_address, u_city, u_state, u_zipcode,
                    u_description}

        if len(u_firstname) == 0:
            render_template("error.html")

        for item in fishlist:
            if len(item) == 0:
                render_template("error.html")

        return render_template("index.html")

    # if db.query.filter(username == s_username):
    #    error = "the username already exists please choose a UNIQUE one foo"

    # if db.query(Product).filter(email_address == s_email):
    #    error = "the e-mail is already registered; you probably got hacked lel"

    # else:
    # return redirect(url_for('where to redirect'))

if __name__ == '__main__':
    app.run(debug = True)