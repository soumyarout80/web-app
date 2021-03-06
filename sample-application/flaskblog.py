from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Soumya Ranjan Rout',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 16, 2019'
    },
    {
        'author': 'Sonali Mishra',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 16, 2019'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/login")
def login():
    return render_template('login.html', title='login')

@app.route("/register")
def register():
    return render_template('register.html', title='Register')

@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
