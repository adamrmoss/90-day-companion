"""Server for movie ratings app."""

from flask import Flask

app = Flask(__name__)


# Replace this with routes and view functions!


if __name__ == "__main__":
    # When running server.py, start the webapp
    app.run(host="0.0.0.0", debug=True, port=5001)
