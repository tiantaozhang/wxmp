
from flask import Blueprint
from app.forms.form import NameForm
from flask import flash
from flask import session, redirect, url_for, render_template
from datetime import datetime
from app import sentry

home = Blueprint('home', __name__)

@home.route('/', methods=['GET', 'POST'])
@home.route('/index')
def index():
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
        return redirect(url_for('home.index'))
    return render_template(
        'html/index.html',
        title='home',
        user=user,
        current_time=datetime.utcnow(),
        form=form,
        name=session.get('name'),
        posts=posts)
