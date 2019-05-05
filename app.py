from flask import Flask
from flask import render_template, flash, redirect
import os
from forms import LoginForm
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import models

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.config['SECRET_KEY'] = 'you-will-never-guess'
# ... add more variables here as needed

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Muigel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }, 
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]    
    return render_template('index.html', title='Home', user=user, posts=posts)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

