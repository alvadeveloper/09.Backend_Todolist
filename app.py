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


app = Flask(__name__)
setup_db(app)
db = SQLAlchemy(app)
app.register_blueprint(server, url_prefix="")
  
'''
@TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
'''
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

def create_app(test_config=None):
  # create and configure the app


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

  @app.route('/list', methods=['GET'])
  @requires_auth('get:list')
  def index(self):
    
    q = (db.session.query(Lists).all())

    lists = []

    for d in q:
      lists.append("List ID : "+ str(d.id))

    return jsonify(lists)  


  @app.route('/task', methods=['GET'])
  @requires_auth('get:list')
  def task(self):  

    q = (db.session.query(User, Lists, Task)
            .filter(User.id == Lists.writer_id)
            .filter(Lists.id == Task.list_id)
            .filter(User.id == 1)
            ).all()

    tasks = []

    for d in q:
      tasks.append("Username : " + d[0].username)
      tasks.append("List ID : " + d[1].title)
      tasks.append("Task : "+ d[2].content)
      tasks.append("Completed? : "+d[2].status)
      tasks.append("Task ID : " + str(d[2].id))

      
    return jsonify(tasks)  


  @app.route('/addtask', methods=['GET', 'POST'])
  @requires_auth('post:list')
  def addtask(self):

    data = request.get_json()

    content = data['content']
    status = data['status']
    list_id = data['list_id']

    task = Task(content=content, status=status,list_id=list_id )
    task.insert()

    return jsonify({
      "success": "Task inserted"
      })


  @app.route('/updatetask', methods=['PATCH'])
  @requires_auth('patch:list')
  def update_task(self):

    q = (db.session.query(Task).all())

    if q is None:
        abort(404)

    data = request.get_json()
    task_id = data['id']
    content = data['content']
    status = data['status']

    task = Task(content=content, status=status,id=task_id )
    task.update()

    return jsonify ({
        "success": True 
      })

  return app
