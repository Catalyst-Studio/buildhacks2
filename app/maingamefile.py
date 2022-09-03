from app.crud import Session
from app.models import Game
db = Session()
def check(level: str, code: str):
    with open(f"app/python-levels/{level}.answer", 'r') as f:
        output = ''.join((line) for line in f)
        print(output)
        if output == code:
            return True
        else:
            return False

def addwin(level, user):
    db.query(Game).filter(Game.id == user["gameid"]).update({level: "true"})
    db.commit()
    return True

def getstats(user):
    data = db.query(Game).filter(Game.id == user["gameid"]).first().__dict__
    return data