"""Models for movie ratings app."""

from flask_sqlalchemy import SQLAlchemy
from database import db_name

db = SQLAlchemy()

def connect_to_db(flask_app, db_name=db_name, echo=True):
    db_uri = f'postgresql:///{db_name}'

    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')
