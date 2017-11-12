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

from flask_sqlalchemy import SQLAlchemy
from passlib.hash import bcrypt
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
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
        return "<Users(username ='%s', password='%s', email_address='%s')>" % (self.username, self.password, self.email_address)

    @validates('email_address')
    def check_email(self, key, email):
        assert '@' in email
        return email

    @validates('zip_code')
    def check_zip_code(self,key,zip):
        assert len(str(zip)) == 5
        return zip

class Shelters(db.Model):
    ahelter_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    shelter_name = db.Column(db.String(200), unique=True, nullable=False)
    email_address = db.Column(db.String(80), unique=True, nullable=False)
    state = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(500), nullable=False)

    def validate_password(self, password):
        return bcrypt.verify(password, self.password)

    def __repr__(self):
        return "<Users(username ='%s', password='%s', email_address='%s')>" % (self.username, self.password, self.email_address)

    @validates('email_address')
    def check_email(self, key, email):
        assert '@' in email
        return email

    @validates('zip_code')
    def check_zip_code(self,key,zip):
        assert len(str(zip)) == 5
        return zip
