from src import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User_Cred.query.get(int(user_id))


class User_Cred(db.Model, UserMixin):
    __tablename__ = 'user_cred'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), nullable=True)

    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password
        self.role = 'user'
        
    def get_id(self):
        return self.user_id

    def __str__(self) -> str:
        return f"{self.role}: {self.username} ({self.user_id}))"
    
    
class User(db.Model):
    __tablename__ = 'users'
    
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user_cred.user_id'), primary_key=True, nullable=False)
    fullname = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(255), nullable=True)
    profile_pic = db.Column(db.String(255), nullable=False)
    
    def __init__(self, user_id, fullname, gender,
                 phone, address, profile_pic):
        super().__init__()
        self.user_id = user_id
        self.fullname = fullname
        self.gender = gender
        self.phone = phone
        self.address = address
        self.profile_pic = profile_pic

    def __str__(self) -> str:
        return f"User: {self.fullname} ({self.user_id})"

class User_Logs(db.Model):
    __tablename__ = "user_logs"

    log_user_id = db.Column(db.Integer, db.ForeignKey(
        'user_cred.user_id'), primary_key=True, nullable=False)
    last_login_date = db.Column(db.Date, nullable=True)
    last_login_time = db.Column(db.Time, nullable=True)
    last_profile_update_date = db.Column(db.Date, nullable=True)
    last_profile_update_time = db.Column(db.Time, nullable=True)
    reg_date = db.Column(db.Date, nullable=False)
    reg_time = db.Column(db.Time, nullable=False)
    
    def __init__(self, log_user_id, reg_date, reg_time):
        super().__init__()
        self.log_user_id = log_user_id
        self.reg_date = reg_date
        self.reg_time = reg_time
    
    def __str__(self) -> str:
        return f"User: ({self.log_user_id}), REG @ {self.reg_date} {self.reg_time}"

class Product(db.Model):
    __tablename__ = 'products'

    product_id = db.Column(db.Integer, primary_key=True)
    product_user_id = db.Column(db.Integer, db.ForeignKey(
        'user_cred.user_id'), nullable=False)
    product_name = db.Column(db.String(255), nullable=False)
    product_type = db.Column(db.String(4), nullable=False)
    product_desc = db.Column(db.TEXT, nullable=True)
    product_pic = db.Column(db.String(255), nullable=True)
    price_range = db.Column(db.String(255), nullable=False)

    def __init__(self, product_user_id, product_name, product_type,
                 product_desc, product_pic, price_range):
        super().__init__()
        self.product_user_id = product_user_id
        self.product_name = product_name
        self.product_type = product_type
        self.product_desc = product_desc
        self.product_pic = product_pic
        self.price_range = price_range
        
    def __str__(self) -> str:
        return f"Product: {self.product_name} ({self.product_id})"
        
class Product_Status(db.Model):
    __tablename__ = 'product_status'
    
    product_id = db.Column(db.Integer, db.ForeignKey(
        'products.product_id'), primary_key=True, nullable=False)
    condition = db.Column(db.String(10), nullable=False)
    entry_date = db.Column(db.Date, nullable=False)
    entry_time = db.Column(db.Time, nullable=False)
    last_update_date = db.Column(db.Date, nullable=False)
    last_update_time = db.Column(db.Time, nullable=False)
    
    
    def __init__(self, product_id, condition, entry_date, entry_time,
                 last_update_date, last_update_time):
        super().__init__()
        self.product_id = product_id
        self.condition = condition
        self.entry_date = entry_date
        self.entry_time = entry_time
        self.last_update_date = last_update_date
        self.last_update_time = last_update_time
        
    def __str__(self) -> str:
        return f"Product ({self.product_id})@ {self.entry_date}"
        

class Bets(db.Model, UserMixin):
    __tablename__ = 'bets'

    bet_id = db.Column(db.Integer, primary_key=True)
    bet_user_id = db.Column(db.Integer, db.ForeignKey('user_cred.user_id'), nullable=False)
    bet_product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=False)
    bet_amount = db.Column(db.Float, primary_key=True)
    bet_date = db.Column(db.Date, nullable=False)
    bet_time = db.Column(db.Time, nullable=False)

    def __init__(self, bet_user_id, bet_product_id, bet_amount, bet_date, bet_time):
        super().__init__()
        self.bet_user_id = bet_user_id
        self.bet_product_id = bet_product_id
        self.bet_amount = bet_amount
        self.bet_date = bet_date
        self.bet_time = bet_time

    def __str__(self) -> str:
        return f"Bet: {self.bet_id} ({self.bet_amount}))"
