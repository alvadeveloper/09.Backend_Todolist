import os
from flask import Flask, request, abort, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import setup_db, TodoList, User

def create_app(test_config=None):
  # create and configure the app
  application = app = Flask(__name__)
  setup_db(app)
  db = SQLAlchemy(app)	

  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''

  cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''

  @app.after_request
  def after_request(response):
  	response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization, true')
  	response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
  	return response


  '''
	Set up routes for app
  '''

  @app.route('/', methods=['GET'])
  def index():
   return "Hello World"





if __name__ == '__main__':
    app.run(debug=True)