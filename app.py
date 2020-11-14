from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL #For MySQL
import MySQLdb.cursors #For MySQL
import re

app = Flask(__name__)

#connection details for mysql
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'StreamingSite'

#initializing MySQL
mysql = MySQL(app)

@app.route('/')
def accueil():
    return render_template('accueil.html')


@app.route('/')
def login():
    return render_template()