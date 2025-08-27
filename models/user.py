from sqlalchemy import Column, Integer, String
from .base import Base
from passlib.context import CryptContext # Import new package
from datetime import datetime, timedelta, timezone 
import jwt 

from config.environment import jwt_secret

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserModel(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=True)  # Add new field for storing the hashed password

    def set_password(self, password: str):
        self.password_hash = pwd_context.hash(password)

     
    def verify_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.password_hash)

    def generate_token(self):
        # Define the payload
        payload = {
            "exp": datetime.now(timezone.utc) + timedelta(days=1),  # Expiration time (1 day)
            "iat": datetime.now(timezone.utc),  # Issued at time
            "sub": self.id,  # Subject - the user ID
        }

        # Create the JWT token
        token = jwt.encode(payload, jwt_secret, algorithm="HS256")

        return token