"""Script to seed database."""

import os
from database import db_name

os.system(f'dropdb {db_name} --if-exists')
os.system(f'createdb {db_name}')

import model
import server

model.connect_to_db(server.app)

# Updates the database schema
model.db.create_all()

from crud import create_user

# Create users
admin = create_user('admin@90day.org', 'abc123')

# TODO: use create methods to add objects to database, committing
#       database sessions as needed
