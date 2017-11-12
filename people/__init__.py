import sys
sys.path.insert(0, '/home/russ/Desktop/hackathon')

from flask import Flask , render_template
from people.models.models import db
from people.views.views import main

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pen226@localhost/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'penis'
db.init_app(app)


app.register_blueprint(main, url_prefix='/main')
