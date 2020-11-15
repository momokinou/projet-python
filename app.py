from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from database import *

engine = create_engine('mysql+pymysql://root:@localhost/StreamingSite')

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
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
    session = sessionmaker(bind=engine)
    s = session()
    result = s.query(Manga).filter(or_(Manga.title.like("%%" + POST_TITLE + "%%"), Manga.alt_title.like("%%" + POST_TITLE + "%%")))

    for row in result:
        print(row.title)
        return logout()
    else:
        return render_template('404.html', manga=POST_TITLE)


@app.route("/home", methods=['POST'])
def manga():
    POST_TITLE = str(request.form['manga'])
    session = sessionmaker(bind=engine)
    s = session()
    result = s.query(Manga).filter(Manga.title)
    for row in result:
        print(row.title)


@app.route("/manga", methods=['POST'])
def read():
    POST_PAGE = str(request.form['manga'])
    query = engine.execute("SELECT title FROM chapter c, INNER JOIN manga m ON c.id_manga = m.id")
    session = sessionmaker(bind=engine)
    s = session()
    result = s.query(Chapter).filter(Manga.title.like('%ンピ%'), Manga.title.like('%ンピ%'))
    for row in result:
        print(row.title)


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()
