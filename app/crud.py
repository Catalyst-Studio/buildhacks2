from sqlalchemy import create_engine
from config import DATABASE_URI_USERS
from models import Base
from sqlalchemy.orm import sessionmaker


engine = create_engine(DATABASE_URI_USERS)

Session = sessionmaker(bind=engine)

s = Session()
Base.metadata.create_all(engine)

