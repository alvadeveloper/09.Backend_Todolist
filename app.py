import os
from flask import Flask, request, abort, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_assets import Bundle, Environment
from webassets.filter import get_filter
import random
from flask_cors import cross_origin

from models import setup_db, User, Lists, Task
from server import server
from auth import AuthError, requires_auth

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
  # create and configure the app
  application = app = Flask(__name__)
  setup_db(app)
  db = SQLAlchemy(app)
  app.register_blueprint(server, url_prefix="")
  
  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''

  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
    return response

  '''
	Set up routes for app
  '''
  app.config['SECRET_KEY']= '$R\x87\xa3\xaa\x0eMM\xb6_\x89=,\xd0t\x07\xe0\x18\x95\x9a8|7?'

  @app.route('/', methods=['GET'])
  @requires_auth('get:list')
  def index():
    return "hello world"


  @app.route('/task', methods=['GET'])
  def task():  

    q = (db.session.query(User, Lists, Task)
            .filter(User.id == Lists.writer_id)
            .filter(Lists.id == Task.list_id)
            .filter(User.id == 1)
            ).all()

    userlist = []

    for d in q:
      userlist.append(d[0].username)
      userlist.append(d[1].title)
      userlist.append(d[2].content)
      userlist.append(d[2].status)
      
    print(userlist)

    return jsonify(userlist)

  @app.route('/newuser', methods=['GET', 'POST'])
  def newuser():

    q = (db.session.query(User).all())

    newuser = []

    for d in q:
      newuser.append(d.username)

    print(newuser)

    return jsonify(newuser)
  

  return app


'''

# Testing code

  @app.route('/adduser', methods=['GET','POST'])
  def adduser():

    username = "Anthony"

    user = User(username=username)
    user.insert()

    return jsonify({
      "success": "True"
      })  

  @app.route('/readuser', methods=['GET'])
  def readuser():

    data = User.query.all()
    for d in data:
      print(d.username)

    return jsonify({
        "data" : "data"
      })

  @app.route('/addlist', methods=['GET', 'POST'])
  def addlist():

    title = "List1"
    writer_id = 1

    list = Lists(title=title, writer_id=writer_id)
    list.insert()

    return jsonify({
      "success": "List inserted"
      })


  @app.route('/readlist', methods=['GET'])
  def readlist():

    data = Lists.query.all()

    for d in data:
      print(d.title)
      print(d.writer_id)

    return jsonify({
      "title": d.title,
      "writer_id" : d.writer_id
      })

  @app.route('/addtask', methods=['GET', 'POST'])
  def addtask():

    content = "To complete project 2"
    status = "False"
    list_id= 27

    task = Task(content=content, status=status,list_id=list_id )
    task.insert()

    return jsonify({
      "success": "Task inserted"
      })


  @app.route('/readtask', methods=['GET'])
  def readtask():

    data = Task.query.all()

    for d in data:
      print(d.content)
      print(d.status)
      print(d.list_id)

    return jsonify({
      "content": d.content,
      "status" : d.status,
      "list_id": d.list_id
      })
'''

  





  