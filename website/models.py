from enum import unique
from sqlalchemy.orm import backref, defaultload

from sqlalchemy.sql.expression import false, true
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150), unique=True)
    password =  db.Column(db.String(150))
    date_created =  db.Column(db.DateTime(timezone=True), default=func.now())
    posts = db.relationship('Post', backref='user', passive_deletes=True)
    IMGposts = db.relationship('ImagePost', backref='user', passive_deletes=True)
    rooms =  db.relationship('Room', backref='user', passive_deletes=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    text = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    parent = db.Column(db.Integer, db.ForeignKey('room.id', ondelete='CASCADE'), nullable=False)

class ImagePost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    img = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    cp = db.Column(db.Text, default='default caption')
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    parent = db.Column(db.Integer, db.ForeignKey('room.id', ondelete='CASCADE'), nullable=False)
    

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    info = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    posts = db.relationship('Post', backref='room', passive_deletes=True)
    IMGposts = db.relationship('ImagePost', backref='room', passive_deletes=True)
    participants = db.relationship('User', backref='room', passive_deletes=True)
