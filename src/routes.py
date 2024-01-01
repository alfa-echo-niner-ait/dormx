from src import app
from flask import render_template, request, redirect, url_for, flash

@app.route('/')
def index():
    flash("App running successfully!", category='success')
    return render_template('index.html', title='Home')