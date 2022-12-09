"""Server for movie ratings app."""

from flask import Flask

from model import db, connect_to_db
from crud import create_user

app = Flask(__name__)


# Replace this with routes and view functions!


if __name__ == "__main__":
    # When running server.py, connect the database and start the webapp
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True, port=5001)
