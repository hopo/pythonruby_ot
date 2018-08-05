from flask import Flask, render_template

app = Flask(__name__)
app.config["MONGO_URI"] = 'mongodb://localhost:27017/fla_db'
mongo = PyMongo(app)

@app.route("/")
def home_page():

    return render_template("index.html", item=item)

