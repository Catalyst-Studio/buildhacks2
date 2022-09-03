import os, hashlib
from app import crud
from time import strftime
from base64 import b64encode
import random, string
from validate_email import validate_email as ve

from app.models import User

letters = string.ascii_letters
db = crud.Session()
def get_user(username):
    try:
        userdb = db.query(User).filter(User.username == username).first().__dict__
        return userdb
    except:
        return None


def createuser(username, password, name, tos, email):
    tme = strftime("%a, %d %b %Y %H:%M:%S")
    username = str(username)
    password = str(password)
    name = str(name)
    tos = str(tos)
    email = str(email)
    salt = os.urandom(128)
    print(salt)
    key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    key = b64encode(key).decode('utf-8')
    insert = User(
        name=name,
        username=username,
        email=email,
        salt=salt,
        key=key,
        tos=tos
    )
    db.add(insert)
    db.commit()
    return True


def checkuser(username, password, email):
    username = str(username)
    password = str(password)
    email = str(email)
    try:
        username_check = db.query(User).filter(User.username.ilike(str(username))).first().__dict__
        return "Username already taken!"
    except:
        pass
    try:
        email_check = db.query(User).filter(User.email.ilike(str(email))).first().__dict__
        return "Email already in use!"
    except:
        pass
    if len(username) < 8:
        return "Username too short please enter a username that is at least 8 Characters long!"
    if ve(email, verify=True) == False:
        return "Please enter a valid Email address!"
    else:
        return "good"


def password(password, user_info):
    password = str(password)
    salt = user_info["salt"]
    print(f"Salt: {salt}")
    key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    key = b64encode(key).decode('utf-8')
    print(f"Key: {key}")
    return key
