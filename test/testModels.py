from flask import Flask
import unittest

#from app/main import db
import sys
sys.path.insert(0, '/home/russ/Desktop/hackathon')
from people.models.models import Users, Shelters, db

'''
    creates a user to test Users models
    basic no exception checking
'''
class appDBTests(unittest.TestCase):



    def setUp(self):
        """
        Creates a new database for the unit test to use
        """
        self.new_user = {
            'username' : 'bob123',
            'first' : 'bob',
            'last': 'bobson',
            'email': 'bob@bob.com',
            'state': 'NY',
            'zipCode': 11111,
            'city': 'brooklyn',
            'address': '123 bob st',
            'password': '1234'
        }




    def testquery(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pen226@localhost/db'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(self.app)
        self.app.app_context().push()
        with self.app.app_context():
            db.create_all()
            user = Users(username= self.new_user['username'],fname=self.new_user['first'],lname=self.new_user['last'],
                email_address=self.new_user['email'],state=self.new_user['state'],zip_code=self.new_user['zipCode'],
                address=self.new_user['address'],city=self.new_user['city'],password=self.new_user['password'])

            db.session.add(user)
            db.session.commit()
            db.session.close()
        test =
        assert self.new_user in Users.query.all()
        assert 1 == Users.query.count()


    def tearDown(self):
        """
        Ensures that the database is emptied for next unit test
        """
        with self.app.app_context:
            db.drop_all()

unittest.main()
