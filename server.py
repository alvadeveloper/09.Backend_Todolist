import os
from functools import wraps
import json
from os import environ as env
from werkzeug.exceptions import HTTPException

from dotenv import load_dotenv, find_dotenv
from flask import Flask
from flask import jsonify
from flask import redirect
from flask import Blueprint
from flask import render_template
from flask import session
from flask import url_for
from authlib.integrations.flask_client import OAuth
from six.moves.urllib.parse import urlencode

app = Flask(__name__)

oauth = OAuth(app)

server = Blueprint("server", __name__, static_folder="static",
                   template_folder="template")

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'profile' not in session:
            # Redirect to Login page here
            return redirect('/')
        return f(*args, **kwargs)

    return decorated


auth0 = oauth.register(
    'auth0',
    client_id=os.environ.get('client_id'),
    client_secret=os.environ.get('client_secret'),
    api_base_url=os.environ.get('api_base_url'),
    access_token_url=os.environ.get('access_token_url'),
    authorize_url=os.environ.get('authorize_url'),
    client_kwargs={
        'scope': 'openid profile email',
    },
)


@server.route('/login')
def login():
    return redirect(os.environ.get('REDIRECT_URL'))


@server.route('/callback')
def callback_handling():
    # Handles response from token endpoint
    auth0.authorize_access_token()
    resp = auth0.get('userinfo')
    userinfo = resp.json()

    # Store the user information in flask session.
    session['jwt_payload'] = userinfo
    session['profile'] = {
        'user_id': userinfo['sub'],
        'name': userinfo['name'],
        'picture': userinfo['picture']
    }
    return jsonify({
        "success": true
    })


@server.route('/dashboard')
@requires_auth
def dashboard():
    return render_template('dashboard.html',
                           userinfo=session['profile'],
                           userinfo_pretty=json.dumps(session['jwt_payload'], indent=4))


@server.route('/logout')
def logout():
    # Clear session stored data
    session.clear()
    # Redirect user to logout endpoint
    params = {'client_id': '2MdOSeT1x6aGKdtQPfPGbC9i6r99Ihoq'}
    return redirect(auth0.api_base_url + '/v2/logout?' + urlencode(params))

    return app
