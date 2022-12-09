"""CRUD operations."""

from model import db, User, connect_to_db

def create_user(email, password):
    """Create and return a new user"""

    user = User(email=email, password=password)
    db.session.add(user)
    db.session.commit()

    return user


def get_user_by_email(email):
    """Get the unique user with a given email"""

    user = User.query.filter(User.email == email).first()

    return user


# TODO: add more CRUD operations, as needed


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
