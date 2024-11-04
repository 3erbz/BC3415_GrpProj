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
    scam = db.relationship('Scams')

class Scams (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    user_id = db.Column(db.String, db.ForeignKey ('user.id'))

class Topic (db.Model):
    title = db.Column(db.String(150), unique=True, nullable=False, primary_key=True)
    description = db.Column(db.String)
    thread = db.relationship('Thread')

class Thread (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), unique=True, nullable=False)
    description = db.Column(db.String)
    topic_title = db.Column(db.String, db.ForeignKey ('topic.title'))
    comment = db.relationship ('Comment')

class Comment (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column (db.String, unique=True, nullable=False)
    thread_id = db.Column (db.Integer, db.ForeignKey('thread.id'))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    gemini_comment = db.relationship('GeminiComment')

class GeminiComment (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column (db.String, unique=True, nullable=False)
    thread_id = db.Column (db.Integer)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    comment_id = db.Column(db.Integer, db.ForeignKey ('comment.id'))