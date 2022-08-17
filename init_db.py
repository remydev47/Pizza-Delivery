from database import engine, Base
from model import  User,Order

Base.metadata.create_all(bind=engine)