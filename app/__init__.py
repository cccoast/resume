from flask import Flask
from werkzeug.contrib.fixers import ProxyFix
xapp = Flask(__name__)
xapp.wsgi_app = ProxyFix(xapp.wsgi_app)
from app import views