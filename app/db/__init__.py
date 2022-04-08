from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

database = Blueprint('database', __name__,)

@database.cli.command('create')
def init_db():
    db.create_all()