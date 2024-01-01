from flask import Flask
from flask_mysqldb import MySQL


app = Flask(__name__)
app.secret_key = '9a49156d8b606b6133a558cef77f09c4'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_PORT'] = '3306'
app.config['MYSQL_DB'] = 'dormx'
app.config['MYSQL_CHARACTERSET'] = 'utf8mb4'
app.config['MYSQL_COLLATION'] = 'utf8mb4_0900_ai_ci'


mysql = MySQL(app)

from src import routes
