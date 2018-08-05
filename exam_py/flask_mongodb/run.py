from flask import Flask
from flask_mongoalchemy import MongoAlchemy

app = Flask(__name__)
app.config['MONGOALCHEMY_DATABASE'] = 'fla_db'
# app.config['MONGOALCHEMY_CONNECTION_STRING'] = 'mongodb://hpark:park@localhost:27017/fla_db'

db = MongoAlchemy(app)


class Author(db.Document):
    name = db.StringField()

