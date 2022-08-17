from database import Base
from sqlalchemy import Column,Integer,Boolean,Text,String

class User(Base):
   __tableuser__='user'
   id=Column(Integer,primary_key=True)
   username=Column(String(25), unique=True)
   email=Column(String(25),unique=True)