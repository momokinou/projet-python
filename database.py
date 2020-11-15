from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship, backref

# create link for connexion into db
engine = create_engine('mysql+pymysql://root:@localhost')
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
    nickname = Column(Text)
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


# create a Session
"""Session = sessionmaker(bind=engine)
session = Session()"""

engine.execute("INSERT INTO users(nickname, password, email, gender, id_language) VALUES ('vani', 'supervani', 'vani@gmail.fr', 'male', 14), ('hamtoé', 'jambon94', 'hamtoé@mail.com', 'male', 14), ('superuser', 'jesuissuperuser', 'user@user.fr', 'unknown', 28), ('moi', 'lui', 'elle@onnesaitplus.net', 'unknown', 5), ('Jacqueline', 'monchienestblanc', 'jacquelinevillard@hotmail.fr', 'female', 13);")
engine.execute("INSERT INTO language(name) VALUES ('Arabic'), ('Bengali'), ('Bulgarian'), ('Burmese'), ('Catalan'), ('Chinese(Simp)'), ('Chinese(Hong-Kong)'), ('Czech'), ('Danish'), ('Dutch'), ('English'), ('Filipino'), ('Finnish'), ('French'), ('German'), ('Greek'), ('Hebrew'), ('Hindi'), ('Hungarian'), ('Indonesian'), ('Italian'), ('Japanese'), ('Korean'), ('Lithuanian'), ('Malay'), ('Mongolian'), ('Norwegian'), ('Other'), ('Persian'), ('Polish'), ('Portuguese(BR)'), ('Portuguese(PT)'), ('Romanian'), ('Russian'), ('Serbo-Russian'), ('Spanish(ES)'), ('Spanish(LATAM)'), ('Swedish'), ('Thai'), ('Turkish'), ('Ukrainian'), ('Vietnamese');")
engine.execute("INSERT INTO manga(title, alt_title, category, description, release_date, ending_date, studio, nbr_volume, nbr_chap) VALUES ('ワンピース', 'One Piece', 'Shonen', \"Gloire, fortune et puissance, c'est ce que possédait Gold Roger, le tout puissant roi des pirates, avant de mourir sur l'échafaud. Mais ses dernières paroles ont éveillées bien des convoitises, et lança la fabuleuse ère de la piraterie, chacun voulant trouver le fabuleux trésor qu\'il disait avoir laissé. A 17 ans, Luffy prend la mer dans une petite barque avec pour but de réunir un équipage de pirates, mais de pirates pas comme les autres, qui devront partager sa conception un peu étrange de la piraterie. L'aventure est lancée.\", '1997-12-24', '2020-04-03', 'Shueisha', 97, 974), ('나 혼자만 레벨업', 'Solo Leveling, Only I level up, Na Honjaman Level Up', 'Shonen', \"Sung Jin Woo est considéré comme le plus faible des Chasseurs de rang E... Autrement dit le plus faible parmi les faibles. Il est tellement faible qu'il est surnommé par ses confrères, le « Faible ». Avec une équipe de Chasseurs, il se rend dans un donjon de rang D. Malheureusement, l\'équipe se retrouve piégée dans une salle avec des monstres qui ne sont pas du tout du niveau du donjon... S\'en suit un massacre... Et Sung Jin Woo, aux portes de la mort arrive à acquérir une capacité pour le moins étrange...\", '2019-09-26', '2020-08-27', 'D&C Media, Kakao', 3, 126);")
engine.execute("INSERT INTO chapter (id, nbr_chapter, title, id_manga, id_language) VALUES(1, 1, 'Romance Dawn', 4, 11),(2, 1, 'They call him Straw Hat Luffy', 4, 11),(3, 1, '', 5, 11),(4, 1, '', 5, 14);")
"""user = User(username = "admin", password = "password")
session.add(user)

user = User(username = "python", password = "python")
session.add(user)

user = User(username = "jumpiness", password = "python")
session.add(user)"""

# commit the record the database
#session.commit()