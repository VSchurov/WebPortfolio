from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///application/test.db")
Session = sessionmaker(autocommit=False,
                       autoflush=False,
                       bind=engine)
Base = declarative_base()
Base.metadata.create_all(engine)
