from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, FieldList
from wtforms.validators import DataRequired, Optional


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')

class TextInput(FlaskForm):
    title = StringField('Review', validators=[Optional()])
    body = TextAreaField('Text', validators=[DataRequired()])
    submit = SubmitField('Submit review', render_kw={'style':'width:120px; height:40px; color: white; background-color:#000000; border-color: black; font: 15px arial;'})

class Prediction():
    values = [0.5, 0.5, 0.5, 0.5, 0.5]
    index = [0, 1, 2, 3, 4]
    message = ""
