from flask import Flask
from flask import Flask, request, session, flash, render_template

@app.route('/')
def homepage():
    return render_template('URL.html')
    
@app.route('/login/', methods = ["POST", "GET"])
def login():
    if request.methods == "POST":
        POST_USERNAME = str(request.form['username'])
        POST_PASSWORD = str(request.form['password'])

    if POST_USERNAME == 'username' and POST_PASSWORD  == 'password': 
            #session['logged_in'] = true:
        return redirect(url_for( 'url.html'))               
    else:
        flash('Invalid credientials!. Try Again.')

    #else if request == 'GET'                            

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return homepage()
    


