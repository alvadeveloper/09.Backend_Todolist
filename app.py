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

  app = Flask(__name__)
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
  def index():
    return "Hello World"

  @app.route('/list', methods=['GET'])
  @requires_auth('get:list')
  def list(self):
    
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


  @app.route('/task/update/<int:taskid>', methods=['PATCH'])
  @requires_auth('patch:list')
  def updatetask(self, taskid):

    data = Task.query.filter(Task.id == taskid).one_or_none()

    print (data.content)

    if data is None:
        abort(404)

    body = request.get_json()

    data.content = body['content']
    data.status = body['status']
    data.update()

    return jsonify ({
        "success": True,
        "Task Updated" : True
      })

  @app.route('/task/delete/<int:taskid>', methods=['DELETE'])
  @requires_auth('delete:list')
  def deletetask(self, taskid):

    data = Task.query.filter(Task.id == taskid).one_or_none()

    if data is None:
        abort(404)

    data.delete()

    return jsonify({
        "success": True,
        "Task Deleted": True
        })


  @app.errorhandler(422)
  def unprocessable(error):
        return jsonify({
                    "success": False, 
                    "error": 422,
                    "message": "unprocessable"
                    }), 422

  @app.errorhandler(404)
  def not_found(error):
        return jsonify({
                        "success": False, 
                        "error": 404,
                        "message": "resource not found"
                        }), 404

  @app.errorhandler(400)
  def bad_request(error):
        return jsonify({
                        "success": False, 
                        "error": 400,
                        "message": "bad request"
                        }), 400

  @app.errorhandler(405)
  def methodnotallowed(error):
        return jsonify({
                        "success": False, 
                        "error": 405,
                        "message": "not allowed"
                        }), 405

  '''
  @TODO implement error handler for AuthError
        error handler should conform to general task above 
  '''

  @app.errorhandler(401)
  def unauthorized(error):
        return jsonify({
                        "success": False, 
                        "error": 401,
                        "message": "Unauthorized"
                        }), 401



  return app
