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


class Country(db.Model):
    """One of the world's countries"""
    __tablename__ = 'countries'

    country_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False, unique=True)

    tv_stars = db.relationship('TvStar', back_populates='country')

    def __repr__(self):
        return f'<Country country_id={self.country_id} name={self.name}>'


class TvSeries(db.Model):
    """The 90 Day Fiancé series or one of its spinoffs"""
    __tablename__ = 'tv_series'

    tv_series_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(128), nullable=False, unique=True)

    tv_seasons = db.relationship('TvSeason', back_populates='tv_series')

    def __repr__(self):
        return f'<TvSeries tv_series_id={self.tv_series_id} name={self.name}>'


class TvSeason(db.Model):
    """A season of a particular series"""
    __tablename__ = 'tv_seasons'

    tv_season_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tv_series_id = db.Column(db.Integer, db.ForeignKey('tv_series.tv_series_id'))

    ordinal = db.Column(db.Integer, index=True)

    tv_series = db.relationship('TvSeries', back_populates='tv_seasons')
    tv_episodes = db.relationship('TvEpisode', back_populates='tv_season')

    def __repr__(self):
        return f'<TvSeason tv_season_id={self.tv_season_id} ordinal={self.ordinal}>'


class TvEpisode(db.Model):
    """An episode of a particular series and season"""
    __tablename__ = 'tv_episodes'

    tv_episode_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tv_season_id = db.Column(db.Integer, db.ForeignKey('tv_seasons.tv_season_id'))

    ordinal = db.Column(db.Integer, index=True)
    name = db.Column(db.String(128), nullable=False)

    tv_season = db.relationship('TvSeason', back_populates='tv_episodes')
    tv_stars = db.relationship('TvStarEpisode', back_populates='tv_episode')

    def __repr__(self):
        return f'<TvEpisode tv_episode_id={self.tv_episode_id} name={self.name}>'


class TvStar(db.Model):
    """A television star appearing on 90 Day Fiancé and / or other series"""
    __tablename__ = 'tv_stars'

    tv_star_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.country_id'))

    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)

    country = db.relationship('Country', back_populates='tv_stars')
    tv_episodes = db.relationship('TvStarEpisode', back_populates='tv_star')

    def __repr__(self):
        return f'<TvStar tv_star_id={self.tv_star_id} name={self.name}>'


class TvStarEpisode(db.Model):
    """A television star appearing on a television episode"""
    __tablename__ = 'tv_star_episodes'

    tv_star_episode_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tv_star_id = db.Column(db.Integer, db.ForeignKey('tv_stars.tv_star_id'))
    tv_episode_id = db.Column(db.Integer, db.ForeignKey('tv_episodes.tv_episode_id'))

    name = db.Column(db.String(128), nullable=False, unique=True)

    tv_star = db.relationship('TvStar', back_populates='tv_episodes')
    tv_episode = db.relationship('TvEpisode', back_populates='tv_stars')

    def __repr__(self):
        return f'<TvStarEpisode tv_star_episode_id={self.tv_star_episode_id}>'


def connect_to_db(flask_app, db_name=db_name, echo=True):
    db_uri = f'postgresql:///{db_name}'

    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')
