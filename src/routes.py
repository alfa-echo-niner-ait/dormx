import datetime

from src import app, db
from flask import render_template, redirect, url_for, flash
from flask_login import login_user
from src.forms import RegistrationForm, LoginForm
from src.models import User, User_Cred


@app.route('/')
def index():
    return render_template('index.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        
        log_user = User_Cred.query.filter_by(username=username).first()
        if log_user and password == log_user.password:
            login_user(log_user, remember)
            flash("Login Successfull!", category="success")
            return redirect(url_for('index'))
        else:
            flash(f'Login Failed! Please check Username/Password', category='danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    flash("Logout successfull!", "warning")
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        fullname = form.fullname.data
        gender = form.gender.data
        phone = form.phone.data
        address = form.address.data
        profile_pic = "male_default.png" if (gender == "Male") else "female_default.png"
        reg_date = datetime.datetime.now().strftime("%Y/%m/%d")
        reg_time = datetime.datetime.now().strftime("%H:%M:%S")
        
        new_user = User(username, fullname, gender, phone, address, reg_date, reg_time, profile_pic)
        db.session.add(new_user)
        db.session.commit()

        regged_user = User.query.filter_by(username=username).first()
        new_cred = User_Cred(regged_user.user_id, username, password)
        db.session.add(new_cred)
        db.session.commit()

        flash(f'Your account has been created successfully!', category='info')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register New Account', form=form)


@app.route('/add_item')
def add_item():
    return render_template('add_item.html', title='Add New Product')
