from sqlalchemy import Column, Integer, String
from ..database import Base

# User model defines the structure of the 'users' table in the database.
class User(Base):
    # Table name in the database
    _tablename_ = 'users'
    # Primary key column for unique identification of users
    id = Column(Integer, primary_key=True, index=True)
    # Email column which must be unique and not null
    email = Column(String(255), unique=True, nullable=False)
    # Password column for storing user passwords
    password = Column(String(255), nullable=False)
    token = Column(String(255), nullable=True)  # For authentication