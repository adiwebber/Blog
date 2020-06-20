from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [
    {
        'author': 'Aditya Aggarwal',
        'title': 'BlogPost 1',
        'content': 'Hey There',
        'date_posted': '14/06/2020'
    },
    {
        'author': 'Aditya ',
        'title': 'BlogPost 2',
        'content': 'Hello here',
        'date_posted': '15/06/2020'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'Passed Title')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for { form.username.data }', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("Successfully logged in!", 'success')
            return redirect(url_for('home'))
        else:
            flash("Username or Password incorrect", 'danger')
    return render_template('login.html', form=form)
