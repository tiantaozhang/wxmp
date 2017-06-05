# -*- coding: utf-8 -*-

import logging
from flask import Flask
from raven.contrib.flask import Sentry
import config.config as cf
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
# app.config.from_object('config')
app.config.from_pyfile('../config/config.py')

sentry = Sentry(dsn=cf.SENTRY_SECRECT, logging=True, level=logging.DEBUG)


def create_app():
    sentry.init_app(app)
    bootstrap = Bootstrap(app)
    moment = Moment(app)

    from app.views.login import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from app.views.wx import wx as wx_blueprint
    app.register_blueprint(wx_blueprint, url_prefix='/wx')

    from app.views.home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from app.views.errors import error as error_blueprint
    app.register_blueprint(error_blueprint)

    return app

