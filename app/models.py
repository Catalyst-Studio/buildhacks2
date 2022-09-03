from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, LargeBinary

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String)
    email = Column(String)
    salt = Column(LargeBinary)
    key = Column(String)
    tos = Column(String)
    gameid = Column(String)

    def __repr__(self):
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "email": self.email,
            "tos": self.tos
        }

class Game(Base):
    __tablename__ = "game"
    id = Column(String,  primary_key=True)
    one = Column(String)
    two = Column(String)
    three = Column(String)
    four = Column(String)
    five = Column(String)
    six = Column(String)
    seven = Column(String)
    eight = Column(String)
    nine = Column(String)
    ten = Column(String)
    eleven = Column(String)
    twelve = Column(String)
    thirteen = Column(String)
    fourteen = Column(String)
    fifteen = Column(String)
    sixteen = Column(String)
