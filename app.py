from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from database import *

engine = create_engine('mysql+pymysql://root:@localhost/StreamingSite')

app = Flask(__name__)
app.secret_key = os.urandom(12)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('index.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
    
    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    result = query.first()
    if result:
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()

@app.route("/search", methods=['POST'])
def search():
    POST_TITLE = str(request.form['search'])
    query = engine.execute("SELECT title FROM manga WHERE title LIKE \"manga\"")
    

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()