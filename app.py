from flask import Flask
from flask import Flask, request, session, flash, render_template, redirect, url_for

@app.route('/')
def homepage():
    return render_template('index.html')
    
@app.route('/login/', methods = ["POST", "GET"])
def login():
    if request.methods == "POST":
        POST_USERNAME = str(request.form['username'])
        POST_PASSWORD = str(request.form['password'])
   if registered_user = User.query.filter_by(username=POST_USERNAME,password=POST_PASSWORD).first()
   return redirect(for_url( 'url.html'))
   else:
        flash('Invalid credientials!. Try Again.')

    #else if request == 'GET'                            

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return render_template('index.html')
    


