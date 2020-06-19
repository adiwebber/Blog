from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'a6d4c206873961514ec69759a9b6b4f7'

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

if __name__ == '__main__':
    app.run(debug=True)