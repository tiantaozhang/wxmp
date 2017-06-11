# -*- coding: utf-8 -*-

from flask import request
from flask import render_template, session, redirect, url_for, flash
from app.forms.form import LoginForm
from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/user/<name>', methods=['GET'])
def user(name):
    return render_template('html/user.html', name=name)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('html/login.html',
                           title='Sign In',
                           form=form)


@auth.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>
    '''


@auth.route('/signin', methods=['POST'])
def signin():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>bad username or password.</h3>'
