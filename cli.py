import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Body, Fish

DB = "sqlite:///bodies.db"

engine = create_engine(DB)
Session = sessionmaker(bind=engine)
session = Session()

def innit_db():
    Base.metadata.create_all(engine)
    print("Batabase Intialized")

# create a water body 

def create_body():
    name = input("enter water body name: ")
    type = input("enter water body type: ")
    water_body = Body(name=name, type=type)
    session.add(water_body)
    session.commit()
    print (f"The water body '{name}' has been created with the ID {water_body.id}")

# update the water body

def update_body():
    