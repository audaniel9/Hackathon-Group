from flask_sqlalchemy import SQLAlchemy
from passlib.hash import bcrypt
from sqlalchemy import validates

db = SQLAlchemy(app)
'''users model
    - id
	- last name
	- first name
    - username
    - password
    - email address
    - state
    - city
    - zip code
    - address
shelters model
    - id
    - shelter name
	- username
    - password
    - email address
    - state
    - city
    - zip code
    - address
    - description
    - jobs(its own model??)
'''
class Users(db.Model):
    id = db.Column(db.Integer, primary_key, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    fname = db.Column(db.String(80), unique=True, nullable=False)
    lname = db.Column(db.String(80), unique=True, nullable=False)
    email_address = db.Column(db.String(80), unique=True, nullable=False)
    state = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(500), nullable=False)

    def validate_password(self, password):
        return bcrypt.verify(password, self.password)

    def __repr__(self):
        return "<User(username ='%s', password='%s', email='%s')>" % (self.username, self.password, self.email)

    @validates('email_address')
    def check_email(self, key, email):
        assert '@' in email
        return email

    @validates('zip_code')
    def check_zip_code(self,key,zip):
        assert len(str(zip)) == 5
        return zip
#Shelters
class Shleters(db.Model):
    id = db.Column(db.Integer, primary_key, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    shelter_name = db.Column(db.String(200), unique=True, nullable=False)
    email_address = db.Column(db.String(80), unique=True, nullable=False)
    state = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(500), nullable=False)
    position_point = db.relationship('Position', backref='shleters', lazy = True)

    def validate_password(self, password):
        return bcrypt.verify(password, self.password)

    def __repr__(self):
        return "<User(username ='%s', password='%s', email='%s')>" % (self.username, self.password, self.email)

    @validates('email_address')
    def check_email(self, key, email):
        assert '@' in email
        return email

    @validates('zip_code')
    def check_zip_code(self,key,zip):
        assert len(str(zip)) == 5
        return zip

#must be included into Shelters
class Position(db.Model):
        #location shelter name and all that other stuff should be comming
        id = db.Column(db.Integer, primary_key, autoincrement=True)
        job_disc = db.Column(db.String(500), unique=True, nullable=False)
        positions_to_fill = db.Column(db.Integer, nullable=False)
        position_req = db.Column(db.String(500), unique = True, nullable=False)
        shelter_id = db.Column(db.Integer, db.ForeignKey('Shelters.id'),unique=True,nullable=False)


    def __init__(self, job_disc, positions_to_fill, postiion_req):
        self.job_disc = job_disc
        self.positions_to_fill = positions_to_fill
        self.position_req = postiion_req
        self.shelter_id = shelter_id;

#this is temp not sure what it does haha :)
@app.route('shelter/view-own-positions')
def show_all():
    return render_template('show_all_for_shelter.html', positions = Position.query.all() )

#link for shelter to enter a new position
@app.route('/shelter/registerpos', methods = ['GET,' 'POST'])
def submitpos():    
    #make sure that the user logged in is classified as shelter so that they can post a submmision
    
    if request.method == 'POST':
        if not #current user is not in a shelter user
            flash('yo your not a person who should access this')
            return redirect(url_for('/'))
        if not request.form['job_disc'] or not request.form['positions_to_fill'] or not requst.form['positions_req']:
            flash('Please enter all the fields', 'error')
        else:
            postions = postions(request.form['job_disc'], request.form['positions_to_fill'], request.form['positions_to_fill'])
            #before we do this we need to find out how to link the id with the position
            #by doing this we will link the shelter with the position
            db.session.add(postions)
            db.session.commit()
            flash('Record was successfully added')
            #this will hopefully redirect them to the page that displays all 
            #the current logged in shelters job page
            return redirect(url_for('show_all_for_shelter'))

        return render_template('submitpos.html')

#link for viewing ALL of the position listings.
@app.route('/view-positions')
def show_all():
    #i want it also not users if they are not logged in
    #might be written in the wrong way I want it to return the whole position list to 
    return render_template('show_all_for_shelter.html', position = Position.query.all() )

@app.route()