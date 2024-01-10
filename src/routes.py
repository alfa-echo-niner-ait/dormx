from src import app, db, helper
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, current_user, logout_user, login_required
from src.forms import RegistrationForm, LoginForm, UpdateProfileForm, AddProductForm, UpdateProductForm, BetForm
from src.models import User, User_Cred, User_Logs, Product, Product_Status, Bets


@app.route('/')
def index():
    page_num = request.args.get('page', 1, int)
    items = Product.query.join(
        Product_Status, Product.product_id == Product_Status.product_id
    ).order_by(Product.product_id.desc()).add_columns(
        Product.product_name, Product.product_id, Product.product_type, Product.price_range,
        Product.product_pic, Product_Status.condition
    ).paginate(page=page_num, per_page=8)
    products = Product.query.order_by(
        Product.product_id.desc()).paginate(page=page_num, per_page=8)
    return render_template('index.html', title='Home', products=items)


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdateProfileForm()
    user = User.query.filter_by(user_id=current_user.user_id).first()
    user_log = User_Logs.query.filter_by(
        log_user_id=current_user.user_id).first()

    profile_img = url_for(
        'static', filename='profile_pics/' + user.profile_pic)

    if form.validate_on_submit():
        date_now, time_now = helper.get_datetime()

        if form.profile_pic.data:
            picture_file = helper.save_profile_picture(form.profile_pic.data)
            user.profile_pic = picture_file
        user.fullname = form.fullname.data
        user_log.last_profile_update_date = date_now
        user_log.last_profile_update_time = time_now

        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('profile'))

    elif request.method == 'GET':
        form.fullname.data = user.fullname
        form.gender.data = user.gender
        form.phone.data = user.phone
        form.address.data = user.address

    return render_template('profile.html', title='Profile',
                           form=form, user=user, log=user_log, profile_img=profile_img)


@app.route('/user/<int:user_id>', methods=['GET', 'POST'])
@login_required
def user(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    return render_template('user.html', title=user.fullname, user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data

        logged_user = User_Cred.query.filter_by(username=username).first()
        if logged_user and password == logged_user.password:
            login_user(logged_user, remember)

            user_log = User_Logs.query.filter_by(
                log_user_id=current_user.user_id).first()

            date_now, time_now = helper.get_datetime()

            user_log.last_login_date = date_now
            user_log.last_login_time = time_now

            db.session.commit()

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
        profile_pic = "male_default.png" if (
            gender == "Male") else "female_default.png"
        reg_date, reg_time = helper.get_datetime()

        new_user_cred = User_Cred(username, password)
        db.session.add(new_user_cred)
        db.session.commit()

        regged_user = User_Cred.query.filter_by(username=username).first()
        new_user = User(regged_user.user_id, fullname, gender,
                        phone, address, reg_date, reg_time, profile_pic)
        new_user_log = User_Logs(regged_user.user_id, reg_date, reg_time)

        db.session.add(new_user)
        db.session.add(new_user_log)
        db.session.commit()

        flash(f'Account created successfully!', category='success')
        return redirect(url_for('profile'))
    return render_template('register.html', title='Register New Account', form=form)


@app.route('/add_item', methods=['GET', 'POST'])
@login_required
def add_item():
    form = AddProductForm()
    if form.validate_on_submit():
        product_pic = 'product_default.png'
        if form.product_pic.data:
            picture_file = helper.save_product_picture(form.product_pic.data)
            product_pic = picture_file

        user_id = current_user.user_id
        name = form.name.data
        type = form.type.data
        description = form.description.data
        price_range = form.price_range.data
        entry_date, entry_time = helper.get_datetime()

        new_prod = Product(user_id, name, type, description,
                           product_pic, price_range)
        db.session.add(new_prod)
        db.session.commit()

        product = Product.query.filter_by(product_user_id=user_id).order_by(
            Product.product_id.desc()).first()
        new_prod_status = Product_Status(
            product.product_id, 'Pending', entry_date, entry_time, entry_date, entry_time)
        db.session.add(new_prod_status)
        db.session.commit()

        flash(f'New product added successfully!', category='success')
        return redirect(url_for('user_items', user_id=current_user.user_id))

    return render_template('add_item.html', title='Add New Product', form=form)


# View for single item
@app.route('/item/<int:item_id>', methods=['GET', 'POST'])
def item(item_id):
    form = BetForm()
    product = Product.query.filter_by(product_id=item_id).first()
    bets = Bets.query.filter_by(bet_product_id=item_id
                                ).join(User, Bets.bet_user_id == User.user_id
                                       ).add_columns(Bets.bet_id,
                                                     Bets.bet_amount, Bets.bet_date, Bets.bet_time, User.user_id,
                                                     User.fullname, User.phone, User.profile_pic)

    poster = User_Cred.query.filter_by(user_id=product.product_user_id).first()
    poster_id = poster.user_id
    poster_name = poster.username
    product_st = Product_Status.query.filter_by(product_id=item_id).first()
    
    return render_template('item.html', title=product.product_name,
                           ps_id=poster_id, ps_uname=poster_name,
                           form=form, item=product, item_st=product_st, bets=bets)


# Manage Products List
@app.route('/items/<int:user_id>', methods=['GET', 'POST'])
@login_required
def user_items(user_id):
    page_num = request.args.get('page', 1, int)
    items = Product.query.filter_by(product_user_id=current_user.user_id).join(
        Product_Status, Product.product_id == Product_Status.product_id
    ).order_by(Product.product_id.desc()).add_columns(
        Product.product_name, Product.product_id, Product.product_type, Product.price_range, Product.product_desc, Product.product_pic,
        Product_Status.condition, Product_Status.entry_date, Product_Status.entry_time, Product_Status.last_update_date, Product_Status.last_update_time
    ).paginate(page=page_num, per_page=10)
    total = items.total
    return render_template('item_list.html', title="My Products", items=items, total=total)


# Single Product update page
@app.route('/item/<int:item_id>/update', methods=['GET', 'POST'])
@login_required
def item_update(item_id):
    form = UpdateProductForm()
    product = Product.query.filter_by(product_id=item_id).first()
    product_st = Product_Status.query.filter_by(product_id=item_id).first()

    if current_user.user_id != product.product_user_id:
        flash(f'Access denied!', category='danger')
        return redirect(url_for('item_update', item_id=item_id))

    if form.validate_on_submit():
        if form.product_pic.data:
            picture_file = helper.save_product_picture(form.product_pic.data)
            product.product_pic = picture_file

        date_now, time_now = helper.get_datetime()

        product.product_name = form.name.data
        product.product_type = form.type.data
        product.product_desc = form.description.data
        product.price_range = form.price_range.data

        if form.complete.data:
            product_st.condition = "Completed"

        product_st.last_update_date = date_now
        product_st.last_update_time = time_now

        db.session.commit()
        flash(f'Product has been updated!', category='success')
        return redirect(url_for('item_update', item_id=item_id))

    elif request.method == 'GET':
        form.name.data = product.product_name
        form.type.data = product.product_type
        form.price_range.data = product.price_range
        form.description.data = product.product_desc

    return render_template('item_update.html',
                           title=product.product_name, item=product, item_st=product_st, form=form)


# Product delete handler
@app.route('/item/<int:item_id>/delete', methods=['GET', 'POST'])
@login_required
def item_delete(item_id):
    product = Product.query.filter_by(
        product_id=item_id, product_user_id=current_user.user_id).first()
    if product:
        db.session.delete(product)
        db.session.commit()
        flash("Product has been deleted!", category="warning")
    else:
        flash("You don't have access!", category="danger")
    return redirect(url_for('user_items', user_id=current_user.user_id))


# Bet placing handler
@app.route('/bet/<int:item_id>', methods=['GET', 'POST'])
@login_required
def bet(item_id):
    if request.method == "POST":
        price = request.form.get('price')
        user_id = current_user.user_id
        bet_date, bet_time = helper.get_datetime()

        bet = Bets(user_id, item_id, price, bet_date, bet_time)
        db.session.add(bet)
        db.session.commit()
        flash(f'Your bet of {price} has been placed!', category='warning')

    return redirect(url_for('item', item_id=item_id))
