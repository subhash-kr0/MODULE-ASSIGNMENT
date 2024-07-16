from flask import Flask, render_template, redirect, url_for, flash
from forms import SignupForm, SigninForm
from models import User

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        existing_user = User.find(username)
        if existing_user:
            flash('Username already exists!', 'danger')
        else:
            user = User(username, password)
            user.save()
            flash('Signup successful! Please login.', 'success')
            return redirect(url_for('signin'))
    return render_template('signup.html', form=form)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.find(username)
        if user and user['password'] == password:
            flash(f'Hello, {username}! You have successfully logged in.', 'success')
            return render_template('signin_success.html', username=username)
        else:
            flash('Invalid username or password!', 'danger')
    return render_template('signin.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
