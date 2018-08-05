from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_pymongo import PyMongo


# ? app and app fields, function
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a211bb13913f781c97f25f0bd0c2dbc6'

# *** Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
#app.config["MONGO_URI"] = 'mongodb://localhost:27017/fla_db'
#mongo = PyMongo(app)

from flaskblog import routes
