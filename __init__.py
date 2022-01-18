from flask import Flask
from simpleform.api.views import form
from simpleform.db import Database as db

database = db().db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite3'
    database.init_app(app)
    simpleform.register_blueprint(form)
    return simpleform
