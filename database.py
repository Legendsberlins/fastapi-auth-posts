from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# MySQL connection string
'''
DATABASE_URL defines the connection string to the MySQL database. Replace 'username', 'password', and 'dbname' with actual credentials.
'''
DATABASE_URL = "mysql+mysqlclient://username:password@localhost/dbname"

# SQLAlchemy setup
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency injection for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()