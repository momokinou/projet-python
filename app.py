from flask import (
    Flask, flash, redirect, render_template, request, session, url_for)

from database import Manga, User, create_session, init_db

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = 'secret_key'


# verify if user is logged or not
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('index.html')


@app.route('/login', methods=['POST'])
def do_admin_login():
    """Connection page."""
    db_session = create_session()
    user = (
        db_session.query(User)
        .filter(User.username == request.form['username'])
        .filter(User.password == request.form['password'])
        .first())
    if user:
        session['logged_in'] = True
        return redirect(url_for('manga'))
    else:
        flash('wrong password!')
        return redirect(url_for('home'))


# function for search manga, return 404 if not find
@app.route("/search", methods=['POST'])
def search():
    POST_TITLE = str(request.form['search'])
    s = create_session()
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
        return render_template('404.html', manga=POST_TITLE)


# function printing all mangas in home page
@app.route("/home")
def manga():
    s = create_session()
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


# function printing all users
@app.route("/user-setting")
def setting():
    s = create_session()
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


# function for logout if you're connected
@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


app.cli.add_command(init_db)
