import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json


database_path = os.environ.get('DATABASE_URL')

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), nullable=False)
    lists = db.relationship('Lists', backref='writer')

    def __init__(self, username):
        self.username = username

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Lists(db.Model):
    __tablename__ = 'lists'

    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=False)
    writer_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    tasks = db.relationship('Task', backref='belongto')

    def __init__(self, title, writer_id):
        self.title = title
        self.writer_id = writer_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Task(db.Model):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    content = Column(String(80), nullable=False)
    status = Column(String(80), nullable=False)
    list_id = db.Column(db.Integer, db.ForeignKey("lists.id"))

    def __init__(self, content, status, list_id):
        self.content = content
        self.status = status
        self.list_id = list_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
