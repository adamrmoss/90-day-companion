"""Script to seed database."""

import os
from database import db_name

# Drop and recreate database
os.system(f'dropdb {db_name} --if-exists')
os.system(f'createdb {db_name}')

from model import db, connect_to_db
import server

# Connect app to database
connect_to_db(server.app)

# Updates the database schema
db.create_all()

from crud import create_user

# Create users
admin = create_user('admin@90day.org', 'abc123')

# TODO: use create methods to add objects to database, committing
#       database sessions as needed
