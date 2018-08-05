from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


# ? app and app fields, function
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a211bb13913f781c97f25f0bd0c2dbc6'


# *** db1) sqlite using SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# *** db2) MariaDB using SQLAlchemy
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://hpark:park@localhost/flask_db'
#db = SQLAlchemy(app)

# *** db3) MongoDB using PyMongo
#from flask_pymongo import PyMongo
#app.config["MONGO_URI"] = 'mongodb://localhost:27017/fla_db'
#mongo = PyMongo(app)


# *** Bcrypt
bcrypt = Bcrypt(app)

# *** LoginManager
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from flaskblog import routes
