from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship, backref

# create link for connexion into db
engine = create_engine('mysql+pymysql://root:@localhost')

# Drop db
engine.execute("DROP DATABASE IF EXISTS StreamingSite")
# Create db
engine.execute("CREATE DATABASE IF NOT EXISTS StreamingSite CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci")
# Select new db
engine.execute("USE StreamingSite")


Base = declarative_base()


# declaring base
class Language(Base):
    __tablename__ = "language"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))


def __init__(self):
    self.name = name


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(Text)
    password = Column(Text)
    email = Column(Text)
    gender = Column(Enum('male', 'female', 'unknown'))
    id_language = Column(Integer, ForeignKey(Language.id))
    

def __init__(self):
    self.username = username
    self.password = password
    self.email = email
    self.gender = gender
    self.id_language = id_language


class Manga(Base):
    __tablename__ = "manga"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(Text)
    alt_title = Column(Text)
    category = Column(String(255))
    description = Column(Text)
    release_date = Column(Date)
    ending_date = Column(Date)
    studio = Column(String(255))
    nbr_volume = Column(Integer)
    nbr_chap = Column(Integer)


def __init__(self):
    self.title = title
    self.alt_title = alt_title
    self.category = category
    self.description = description
    self.release_date = release_date
    self.ending_date = ending_date
    self.studio = studio
    self.nbr_volume = nbr_volume
    self.nbr_chap = nbr_chap


class Chapter(Base):
    __tablename__  ="chapter"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nbr_chapter = Column(Integer)
    title = Column(String(255))
    id_manga = Column(Integer)
    id_language = Column(Integer, ForeignKey(Language.id))


def __init__(self):
    self.nbr_chapter = nbr_chapter
    self.title = title
    self.id_manga = id_manga
    self.id_language = id_language


# create table
Base.metadata.create_all(engine)


# execute INSERT queries
file = open('./query/use.txt', encoding="utf-8")
use = text(file.read())
engine.execute(use)
file = open('./query/users.txt', encoding="utf-8")
users = text(file.read())
engine.execute(users)
file = open('./query/language.txt', encoding="utf-8")
query = text(file.read())
engine.execute(query)
file = open('./query/manga.txt', encoding="utf-8")
manga = text(file.read())
engine.execute(manga)
file = open('./query/chapter.txt', encoding="utf-8")
chapter = text(file.read())
engine.execute(chapter)
