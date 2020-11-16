**FUNCTIONAL TUTORIAL :**

Before everything,
Think to first run the command: "export FLASK_APP=app.py" or if you are on Windows, via the command prompt: "set FLASK_APP=app.py" ,via PowerShell: "$env:FLASK_APP = "app.py"".
After that, you have to have a MySQL server that is running (via WAMP for exemple).
Initially, the username = "root" and the password = "", you can change this in app.py, line 7 "username:password@localhost".

Finally, you can launch everything with: "py -m flask run"

How to connect to the Streaming Site :
Login : vani
Password : supervani

After you login at the site, you will find all the manga included in our base.
For return to this page, just click on the button "Manga".

How to research :
2 mangas is in this site, which include :
- 나 혼자만 레벨업 - Solo Leveling
- ワンピース - One Piece

You can use either title or alternative title
For our tables, title is the name using their mother language (japanese or korean). 
Alternative titles are others names refering to the manga.

We have an auto-completion for our research. 
You can type what you want, if the string you typed is part of the title or the alternative title, 
your research return the corresponding manga.
Otherwise, a 404 page will inform you that we don't have the manga searched.

For example, the research "Naruto" will return you a 404 error.
In an other hand, the research "O" will return One Piece and Solo Leveling.

The "list users" button will bring you to the current users who have an account on this site.

You can logout at any moment with the button "logout".

**TECHNICAL TUTORIAL :**

Query repertory : this repertory include all the creation and insertion query.

Static and templates repertories (css and html) : its files are used for the front.

app.py : handle http queries. Here are call all the sql query, and the html direction.

database.py : define database creation, creation of tables, and creation of values.
