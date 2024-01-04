from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = '9a49156d8b606b6133a558cef77f09c4'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/dormx'
app.config['SQLALCHEMY_CHARSET'] = 'utf8mb4'
app.config['SQLALCHEMY_COLLATION'] = 'utf8mb4_0900_ai_ci'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'danger'

from src import routes