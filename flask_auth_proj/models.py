from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from __init__ import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
