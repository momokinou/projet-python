from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship, backref

# create link for connexion into db
engine = create_engine('mysql+pymysql://root:@localhost')
# Create db
engine.execute("CREATE DATABASE IF NOT EXISTS StreamingSite")
# Select new db
engine.execute("USE StreamingSite")


Base = declarative_base()


# declaring base
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(4294000000))
    password = Column(String(4294000000))


def __init__(self):
    self.username = username
    self.password = password


class Language(Base):
    __tablename__ = "language"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))


def __init__(self):
    self.name = name


class Manga(Base):
    __tablename__ = "manga"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(4294000000))
    alt_title = Column(String(4294000000))
    category = Column(String(255))
    description = Column(String(4294000000))
    release_date = Column(Date)
    ending_date = Column(Date)
    studio = Column(String(255))
    nbr_volume = Column(Integer)
    nbr_chap = Column(Integer)


def __init__(self):
    self.title = title


# create table
Base.metadata.create_all(engine)


# create a Session
Session = sessionmaker(bind=engine)
session = Session()

user = User(username = "admin", password = "password")
session.add(user)

user = User(username = "python", password = "python")
session.add(user)

user = User(username = "jumpiness", password = "python")
session.add(user)

# commit the record the database
session.commit()