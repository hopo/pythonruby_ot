from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author' : 'Amber Liu',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'April 20, 2018'
    },
    {
        'author' : 'Sooki Nam',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'April 29, 2018'
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
