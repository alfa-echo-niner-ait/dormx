from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SelectField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError
from src.models import User_Cred


class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=100)])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')
    
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

    def validate_username(self, username):
        user = User_Cred.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(f"{username.data} already exist! Please type different username.")

class UpdateProfileForm(FlaskForm):
    current_password = PasswordField('Current Password (Required for changing password)')
    new_password = PasswordField('New Password')
    fullname = StringField('Full Name',
                           validators=[DataRequired(), Length(min=2, max=100)])
    gender = SelectField('Gender',
                         validators=[DataRequired()], choices=[('Male', 'Male'), ('Female', 'Female')])
    phone = StringField('Phone', validators=[DataRequired()])
    address = StringField('Address')
    profile_pic = FileField('Update Picture', validators=[
                        FileAllowed(['jpg', 'jpeg', 'png'])])

    submit = SubmitField('Update')


class AddProductForm(FlaskForm):
    name = StringField('Product Name',
                           validators=[DataRequired(), Length(min=2, max=255)])
    type = SelectField('Product Type',
                         validators=[DataRequired()], choices=[('Buy', 'I want to buy this product'), ('Sell', 'I want to sell this product')])
    description = TextAreaField('Product Description')
    price_range = StringField('Price Range')
    product_pic = FileField('Product Picture', validators=[
                        FileAllowed(['jpg', 'jpeg', 'png'])])

    submit = SubmitField('Add Product')
    
    
