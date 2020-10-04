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

server = Blueprint("server", __name__, static_folder="static", template_folder="template")

app.config['SECRET_KEY'] = '$R\x87\xa3\xaa\x0eMM\xb6_\x89=,\xd0t\x07\xe0\x18\x95\x9a8|7?'

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
    client_id='2MdOSeT1x6aGKdtQPfPGbC9i6r99Ihoq',
    client_secret='HgWL9zAMTlHEfwrRZtVcNYP07EMejOW_xprPnjWR_dGdqvLVpGMcyBN_dDHzws_B',
    api_base_url='https://dev-rp5hh-6z.auth0.com',
    access_token_url='https://dev-rp5hh-6z.auth0.com/oauth/token',
    authorize_url='https://dev-rp5hh-6z.auth0.com/authorize',
    client_kwargs={
        'scope': 'openid profile email',
    },
)


@server.route('/login')
def login():
    return redirect('https://dev-rp5hh-6z.auth0.com/authorize?audience=todo&response_type=token&client_id=2MdOSeT1x6aGKdtQPfPGbC9i6r99Ihoq&redirect_uri=http://localhost:5000')

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
