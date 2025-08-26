# models/base.py
from sqlalchemy import Column, DateTime, Integer, func, String, Boolean
from sqlalchemy.ext.declarative import declarative_base



# Create a base class for all models
Base = declarative_base()
# TeaModel extends SQLAlchemy's 
class BaseModel(Base):

# This is will be used directly to make a 
# Table in PostrSQL 
    __abstract__ = True  # Prevents this class from being mapped to a database table

#   Specifizc colmuns for our Tea Table. 
    id = Column(Integer, primary_key=True, index=True)  # Unique identifier for each record


    created_at = Column(DateTime, default=func.now())  # Timestamp for when the record was created
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())  # Auto-updates on changes
