import click
from flask.cli import with_appcontext
from sqlalchemy import (
    create_engine, Column, Date, Enum, ForeignKey, Integer, String, Text)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = 'mysql+pymysql://root:@localhost'
Base = declarative_base()


class Language(Base):
    __tablename__ = "language"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(Text)
    password = Column(Text)
    email = Column(Text)
    gender = Column(Enum('male', 'female', 'unknown'))
    id_language = Column(Integer, ForeignKey(Language.id))


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


class Chapter(Base):
    __tablename__ = "chapter"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nbr_chapter = Column(Integer)
    title = Column(String(255))
    id_manga = Column(Integer)
    id_language = Column(Integer, ForeignKey(Language.id))


def create_session():
    engine = create_engine(f'{DB_URL}/StreamingSite')
    session = sessionmaker(bind=engine)
    return session()


@click.command("init-db")
@with_appcontext
def init_db():
    engine = create_engine(DB_URL)
    engine.execute("DROP DATABASE IF EXISTS StreamingSite")
    engine.execute("CREATE DATABASE IF NOT EXISTS StreamingSite")
    engine.execute("USE StreamingSite")
    Base.metadata.create_all(engine)
    for line in open('data.sql').readlines():
        engine.execute(line)
    click.echo("Base de données initialisée")
