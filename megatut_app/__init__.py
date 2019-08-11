import sys

sys.path.insert(0, '/afs/.ist.utl.pt/users/6/5/ist176165/web/cgi-bin/flask_env/lib/python3.5/site-packages')

from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from megatut_app import routes