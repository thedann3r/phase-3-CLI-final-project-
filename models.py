from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Body(Base):
    __tablename__ = "water_bodies"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)

    fishies = relationship("Fish", back_populates="water_body")

    def __repr__(self):
        return f"Body(id = {self.id}, name = '{self.name}', type = '{self.type}')"
    
class Fish(Base):
    __tablename__ = "fish"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    population = Column(Integer, nullable=False)
    age = Column(Integer, nullable=False)
    body_id = Column(Integer, ForeignKey("water_bodies.id"))

    water_body = relationship("Body", back_populates="fishies")

    def __repr__(self):
        return f"Fish(id = {self.id}, name = '{self.name}', population = '{self.population}', age = '{self.age}', body_id = {self.body_id})"




    
