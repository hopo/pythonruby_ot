from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

# ? app and app fields, function
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a211bb13913f781c97f25f0bd0c2dbc6'

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


@app.route("/login")
def login():
    template = 'login.html'
    form = LoginForm()
    return render_template(template, title='Login', form=form)



# ! __main__
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
