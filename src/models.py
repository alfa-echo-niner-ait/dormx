from src import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User_Cred.query.get(int(user_id))


class User(db.Model):
    __tablename__ = 'users'
    
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    fullname = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(255), nullable=True)
    reg_date = db.Column(db.Date, nullable=False)
    reg_time = db.Column(db.Time, nullable=False)
    profile_pic = db.Column(db.String(255), nullable=False)
    
    def __init__(self, username, fullname, gender, phone, address, reg_date, reg_time, profile_pic):
        super().__init__()
        self.username = username
        self.fullname = fullname
        self.gender = gender
        self.phone = phone
        self.address = address
        self.reg_date = reg_date
        self.reg_time = reg_time
        self.profile_pic = profile_pic

    def __str__(self) -> str:
        return f"User: {self.fullname} ({self.username})"


class User_Cred(db.Model, UserMixin):
    __tablename__ = 'user_cred'

    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, user_id, username, password):
        super().__init__()
        self.user_id = user_id
        self.username = username
        self.password = password
        
    def get_id(self):
        return self.user_id

    def __str__(self) -> str:
        return f"User: {self.username} ({self.user_id}))"
