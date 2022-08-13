from flask import Flask, jsonify, request, make_response
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config.developmentconfig import config

app = Flask(__name__)
CORS(app, resources={r"/login/*"})
db = SQLAlchemy(app)
ma = Marshmallow()

from routes.api import *

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()