# -*- coding: utf-8 -*-

from flask import request
from flask import render_template, session, redirect, url_for, flash
from flask import Blueprint

error = Blueprint('error', __name__)

@error.errorhandler(404)
def page_not_found(e):
    return render_template('html/404.html'), 404


@error.errorhandler(500)
def internal_server_error(e):
    return render_template('html/500.html'), 500


