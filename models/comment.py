# models/comment.py
from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship
from .base import BaseModel

class CommentModel(BaseModel):

# The name of the table in the database
    __tablename__ = "comments" 

# Unique identifier for the comment
    id = Column(Integer, primary_key=True, index=True)
   
# The text content of the comment
    content = Column(String, nullable=False)  

    # ForeignKey establishes a connection to the teas table
    tea_id = Column(Integer, ForeignKey('teas.id'), nullable=False)

 # Defines the relationship to the TeaModel 
    tea = relationship("TeaModel", back_populates="comments")    
