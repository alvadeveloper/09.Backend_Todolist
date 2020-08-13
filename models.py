import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_name = 'todo'
database_path = "postgres://{}/{}".format('localhost:5432', database_name)

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
	username = Column(String, nullable=False)
	lists = db.relationship('TodoList', backref='writer')

	def __init__(self, username, lists):
		self.username = username
		self.list = lists

	def insert(self):
		db.session.add(self)
		db.session.commit()

	def update(self):
		db.session.commit()

	def delete(self):
		db.session.delete(self)
		db.session.commit()


class TodoList(db.Model):
	__tablename__ = 'todolist'

	id = Column(Integer, primary_key=True)
	title = Column(String(80))
	content = Column(String(300), nullable=False)
	userid = Column(db.Integer, db.ForeignKey(User.id))

	def __init__(self, title, content, userid):
		self.title = title
		self.content = content
		self.userid = userid

	def insert(self):
		db.session.add(self)
		db.session.commit()

	def update(self):
		db.session.commit()

	def delete(self):
		db.session.delete(self)
		db.session.commit()





























	


    