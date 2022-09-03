from sqlalchemy import create_engine
from app.config import DATABASE_URI_USERS
from sqlalchemy.orm import sessionmaker

from app.models import Base


engine = create_engine(DATABASE_URI_USERS)

Session = sessionmaker(bind=engine)

s = Session()
Base.metadata.create_all(engine)

