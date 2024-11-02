from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    # unique = true means there would be no duplicate user
    # db.string (n) = database type, n refers to the max number of characters 
    email = db.Column(db.String (150), unique=True)
    password = db.Column(db.String (150))
    first_name = db.Column(db.String (150))

class Topic (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), unique=True, nullable=False)
    description = db.Column(db.String)

class Comment (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column (db.String, unique=True, nullable=False)
    topicID = db.Column(db.String)
    gemini_comment = db.relationship('GeminiComment')

class GeminiComment (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column (db.String, unique=True, nullable=False)
    topicID = db.Column(db.String)
    comment_id = db.Column(db.Integer, db.ForeignKey ('comment.id'))