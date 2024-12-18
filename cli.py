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
    print("Database Intialized")

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
    body_id = int(input("Enter Water body ID to update: "))
    water_body =session.get(Body, body_id)
    if not water_body:
        print(f"Water body of ID {body_id} does not exist.")
        return
    water_body.name = input(f"Enter new water body name(current: {water_body.name}): ") or water_body.name
    water_body.type = input(f"Enter new water body type(current: {water_body.type}): ") or water_body.type
    session.commit()
    print(f"water body with id {body_id} has been updated succesfully.")

# delete the water body

def delete_body():
    body_id = int(input("Enter water body ID to be deleted: "))
    water_body =session.get(Body, body_id)
    if not water_body:
        print(f"Water body of ID {body_id} does not exist.")
        return
    session.delete(water_body)
    session.commit()
    print(f"water body with id {body_id} has been deleted succesfully.")

def fish_create():
    name = input("Enter name of new fish: ")
    population = input("Enter population of new fish: ")
    age = input("Enter age of new fish: ")
    fish = Fish(name=name, population=population, age=age)
    session.add(fish)
    session.commit
