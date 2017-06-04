# -*- coding: utf-8 -*-

import hashlib

from flask import Flask
from flask import request
from flask import render_template, session, redirect, url_for, flash
from controller.form import LoginForm
from controller.form import NameForm
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from raven.contrib.flask import Sentry
import config.config as cf
import logging

app = Flask(__name__)
# app.config.from_object('config')
app.config.from_pyfile('config/config.py')

bootstrap = Bootstrap(app)
moment = Moment(app)
manager = Manager(app)

sentry = Sentry(dsn=cf.SENTRY_SECRECT,logging=True, level=logging.DEBUG)

@app.route('/', methods=['GET',  'POST'])
@app.route('/index')
def home():
    user = {'nickname': 'tatumn'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    try:
        1 / 0
    except Exception:
        sentry.captureException()
    sentry.captureMessage('hello, world!')
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('home'))
    return render_template('html/index.html', title='home', user=user, current_time=datetime.utcnow(), form=form , name=session.get('name') , posts=posts)


@app.route('/user/<name>', methods=['GET'])
def user(name):
    return render_template('html/user.html', name=name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('html/login.html',
                           title='Sign In',
                           form=form)


@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>
    '''


@app.route('/signin', methods=['POST'])
def signin():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>bad username or password.</h3>'


@app.errorhandler(404)
def page_not_found(e):
    return render_template('html/404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('html/500.html'), 500


@app.route('/wx', methods=['GET', 'POST'])
def handle_wx_token():
    try:
        data = request.args
        if len(data) == 0:
            return "hello, this is handle view"
        print data
        signature = data["signature"]
        timestamp = data["timestamp"]
        nonce = data["nonce"]
        echostr = data["echostr"]
        token = "weilaidav2017"

        list = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, list)
        hashcode = sha1.hexdigest()
        print "handle/GET func: hashcode, signature: ", hashcode, signature
        if hashcode == signature:
            return echostr
        else:
            return "<p>notice: hashcode:%s, signature:%s</p>" % (hashcode, signature)
    except Exception as e:
        return '<h4>"error:" + %s </h4>' % e.message


if __name__ == "__main__":
    sentry.init_app(app)
    app.run(host='0.0.0.0', port=15000, debug=True)
    # manager.run()
