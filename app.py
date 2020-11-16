from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker, create_engine
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
    return manga()


@app.route("/search", methods=['POST'])
def search():
    POST_TITLE = str(request.form['search'])
    session = sessionmaker(bind=engine)
    s = session()
    result1 = s.query(Manga).filter(Manga.title.like("%%" + POST_TITLE + "%%"))
    result2 = s.query(Manga).filter(Manga.alt_title.like("%%" + POST_TITLE + "%%"))
    strTable = render_template('main.html')
    row = ""
    for row in result1:
        if row:
            title = row.title
            alt_title = row.alt_title
            strRW = "<div class=\"title\">" + str(title) + " - " + str(alt_title) + "</div>"
            strTable = strTable + strRW
    for row in result2:
        if row:
            title = row.title
            alt_title = row.alt_title
            strRW = "<div class=\"title\">" + str(title) + " - " + str(alt_title) + "</div>"
            strTable = strTable + strRW
    if row:
            if row.title:
                strTable = strTable + "</div></body></html>"
                hs = open("./templates/search.html", 'w', encoding="utf-8")
                hs.write(strTable)
                hs.close()
                return render_template('search.html')
    else: 
        return render_template('404.html', manga = POST_TITLE)


@app.route("/home")
def manga():
    session = sessionmaker(bind=engine)
    s = session()
    result = s.query(Manga).all()
    strTable = render_template('main.html')
    for row in result:
        title = row.title
        alt_title = row.alt_title
        strRW = "<div class=\"title\">" + str(title) + " - " + str(alt_title) + "</div>"
        strTable = strTable + strRW

    strTable = strTable + "</div></body></html>"
    hs = open("./templates/manga.html", 'w', encoding="utf-8")
    hs.write(strTable)
    hs.close()
    return render_template('manga.html')


@app.route("/user-setting")
def setting():
    session = sessionmaker(bind=engine)
    s = session()
    data = s.query(User).all()
    strTable = render_template('main.html')
    hs = open("./templates/admin.html", 'w', encoding="utf-8")
    hs.write(strTable + "<h1>List User</h1><br>")
    strTable = ""
    for row in data:
        title = row.username
        strRW = "<div>" + str(title) + "</div>"
        strTable = strTable + strRW
    
    strTable = strTable + "<div class=\"notfound-group\"><div class=\"notfound-child\">"
    strTable = strTable + "</div></body></html>"
    hs.write(strTable)
    hs.close()
    return render_template("admin.html")


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()
