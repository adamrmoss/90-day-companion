"""Models for movie ratings app."""

from flask_sqlalchemy import SQLAlchemy
from database import db_name

db = SQLAlchemy()

class User(db.Model):
    """90 Day Companion User"""
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'


# class TvSeries(db.Model):
#     """The 90 Day Fiancé series or one of its spinoffs"""
#     pass


# class TvSeason(db.Model):
#     """A season of a particular series"""
#     pass


# class TvEpisode(db.Model):
#     """An episode of a particular series and season"""
#     pass


# class TvStar(db.Model):
#     """A television star appearing on 90 Day Fiancé and / or other series"""
#     pass


def connect_to_db(flask_app, db_name=db_name, echo=True):
    db_uri = f'postgresql:///{db_name}'

    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')
