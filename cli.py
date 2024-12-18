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
    age = int(input("Enter age of new fish: "))
    body_id = int(input("Enter ID of new fish: "))
    fish = Fish(name=name, population=population, age=age, body_id=body_id)
    session.add(fish)
    session.commit()
    print(f"The fish called '{name}' with ID {fish.id} lives in the water body with ID {body_id}")

def fish_update():
    fish_id = int(input("Enter ID for fish to be updated: "))
    fish = session.get(Fish, fish_id)
    if not fish:
        print(f"fish with ID {fish_id} does not exist")
        return
    fish.name = input(f"Enter new fish name(current: {fish.name}): ") or fish.name
    fish.population = input(f"Enter new fish population(current: {fish.population}): ") or fish.population
    fish.age = int(input(f"Enter new fish age(current: {fish.age}): ")) or fish.age
    new_body_id = input(f"Enter new fish id(current: {fish.body_id}): ") or fish.body_id
    if new_body_id:
        new_id = session.get(Fish, int(new_body_id))
        if not new_id:
            print(f"Water body with ID {new_body_id} does not exist, skipping update")
        else:
            fish.body_id = new_body_id
    session.commit()
    print(f"Fish with ID {fish_id} updated successfully.")

def fish_delete():
    fish_id = int(input("Enter fish you want to delete: "))
    fish = session.get(Fish, fish_id)
    if not fish:
        print(f"Fish with ID {fish_id} does not exist")
        return
    session.delete(fish)
    session.commit()
    print(f"Fish with ID {fish_id} has been deleted succesfully.")

def assign_fish():
    fish_id = int(input("Enter fish ID: "))
    body_id = int(input("Enter water body ID: "))
    fish = session.get(Fish, fish_id)
    body = session.get(Body, body_id)

    if not fish or not body:
        print("Invalid fish id or water body id.")
        return
    fish.body_id = body_id
    session.commit()
    print("Fish assigned to water body successfully.")

def list_fish():
    fish = session.query(Fish).all()
    if not fish:
        print("No fish found")
    for fis in fish:
        print(fis)

def list_body():
    body = session.query(Body).all()
    if not body:
        print("No water body found")
    for bod in body:
        print(bod)

def view_fish_by_body():
    body_id = int(input("Enter body ID to view fish: "))
    body = session.get(Body, body_id)
    if not body:
        print(f"Body with {body_id} does not exist.")
        return
    fish = body.fish
    if not fish:
        print(f"No fish found for body with ID {body_id} .")
        return
    print(f"Fish belongning to the water body: '{body.name}' (ID {body_id}):")
    for fishie in fish:
        print(fishie)