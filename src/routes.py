import datetime
import os
import secrets
from PIL import Image

from src import app, db
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, current_user, logout_user, login_required
from src.forms import RegistrationForm, LoginForm, UpdateProfileForm
from src.models import User, User_Cred


@app.route('/')
def index():
    return render_template('index.html', title='Home')


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdateProfileForm()
    user = User.query.filter_by(username=current_user.username).first()
    profile_img = url_for(
        'static', filename='profile_pics/' + user.profile_pic)
    
    if form.validate_on_submit():
        if form.profile_pic.data:
            picture_file = save_picture(form.profile_pic.data)
            user.profile_pic = picture_file
        user.fullname = form.fullname.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('profile'))
    
    elif request.method == 'GET':
        form.fullname.data = user.fullname
        form.gender.data = user.gender
        form.phone.data = user.phone
        form.address.data = user.address
    
    return render_template('profile.html', title='Profile', form=form, user=user, profile_img=profile_img)


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(
        app.root_path, 'static/profile_pics', picture_fn)

    output_size = (150, 150)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        
        log_user = User_Cred.query.filter_by(username=username).first()
        if log_user and password == log_user.password:
            login_user(log_user, remember)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash(f'Login Failed! Please check Username/Password', category='danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash("Logout successfull!", "info")
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

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

        flash(f'Account created successfully!', category='success')
        flash(f'Update profile if you need any change!', category='info')
        return redirect(url_for('profile'))
    return render_template('profile.html', title='Register New Account', form=form)


@app.route('/add_item')
@login_required
def add_item():
    if not current_user.is_authenticated:
        flash("You must login to continue!", "warning")
        return redirect(url_for('login'))
    return render_template('add_item.html', title='Add New Product')
