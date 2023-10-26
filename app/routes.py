from app import app, db
from flask import render_template, redirect, url_for, flash
# Import the SingUpForm and LoginForm class from forms
from app.forms import SignUpForm, LoginForm
# Import the User model from models
from app.models import User

# Create our first route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/topfive')
def topfive():
    top_five_img = []
    return render_template('topfive.html')


