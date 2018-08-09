from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


# *** INIT
# ? app and app fields, function
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a211bb13913f781c97f25f0bd0c2dbc6'

# *** Database
# db1) sqlite using SQLAlchemy
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#db = SQLAlchemy(app)

# db2) MariaDB using SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://java:oracle@localhost:3306/flask_db'
db = SQLAlchemy(app)

# db3) MongoDB using flask-mongoalchemy
#from flask_mongoalchemy import MongoAlchemy
#app.config['MONGOALCHEMY_DATABASE'] = 'fla_db'
#app.config['MONGOALCHEMY_CONNECTION_STRING'] = 'mongodb://localhost:27017/fla_db'
#db = MongoAlchemy(app)


# *** Bcrypt
bcrypt = Bcrypt(app)

# *** LoginManager
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from flaskblog import routes


