from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=100)])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    fullname = StringField('Full Name',
                           validators=[DataRequired(), Length(min=2, max=100)])
    gender = SelectField('Gender',
                         validators=[DataRequired()], choices=[('Male', 'Male'), ('Female', 'Female')])
    phone = StringField('Phone', validators=[DataRequired()])
    address = StringField('Address')

    submit = SubmitField('Register')
    
    
class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=100)])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    
    submit = SubmitField('Login')
