from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

# ? app and app fields, function
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a211bb13913f781c97f25f0bd0c2dbc6'

# database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}')"


posts = [
    {
        'author': 'Amber Liu',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Sooki Nam',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 29, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    template = 'home.html'
    return render_template(template, posts=posts)


@app.route("/about")
def about():
    template = 'about.html'
    return render_template(template, title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    template = 'register.html'
    form = RegistrationForm()
    # !! if submitted form data is valid
    if form.validate_on_submit():
        # ? what is two parameter of flash()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template(template, title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    template = 'login.html'
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == '1111':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check your email and password!', 'danger')
    return render_template(template, title='Login', form=form)



# ! __main__
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
