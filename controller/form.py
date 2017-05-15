from flask_wtf import  Form
from wtforms import StringField, TextField, BooleanField, PasswordField, SubmitField
from wtforms.validators import Required, Email, Length

class LoginForm(Form):
    name = TextField('name', validators=[Required(), Length(max=15)])
    password = PasswordField('password', validators=[Required()])
    remember_me = BooleanField('Remember_me', default=False)
    submit = SubmitField('Log in')


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')