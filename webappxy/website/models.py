from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    uName = db.Column(db.String(150), unique=True)
    custom_profile_unlocked = db.Column(db.Boolean, default=False)
    notes = db.relationship('Note')
    posts = db.relationship('Post', backref='author', lazy=True)

    # Additional profile fields
    full_name = db.Column(db.String(150))
    bio = db.Column(db.String(255))
    # Add any other fields you need for the user's profile


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
