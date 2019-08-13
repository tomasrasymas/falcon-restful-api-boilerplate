from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from config import config


engine = create_engine(config.DATABASE_URL)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
