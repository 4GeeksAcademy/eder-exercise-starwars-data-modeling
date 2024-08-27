import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    usuarioID = Column(Integer,primary_key=True)
    username = Column(String(40), nullable = False)
    password = Column(String(40),nullable = False)
    fullname = Column(String(200),nullable = False)
    email = Column(String(100),nullable=False)
    created = Column(String(20),nullable=False)
    favorite = relationship('Favorite',backref='usuario',lazy=True)

class Planet(Base):
    __tablename__ = 'planet'
    planetID = Column(Integer,primary_key=True)
    name = Column(String(100),nullable=False)
    diameter =Column(String(100),nullable=False)
    rotation_periord = Column(String(100),nullable=False)
    orbital_period = Column(String(100),nullable=False)
    gravity = Column(String(100),nullable=False)
    population = Column(String(100),nullable=False)
    climate = Column(String(100),nullable=False)
    terrain = Column(String(100),nullable=False)
    surface_water = Column(String(100),nullable=False)
    created = Column(String(100),nullable=False)
    edited = Column(String(100),nullable=False)
    favorite = relationship('Favorite',backref='planet',lazy=True)


class Vehicle(Base):
    __tablename__ = 'vehicle'
    vehicleID = Column(Integer,primary_key=True)
    name = Column(String(100),nullable=False)
    model =  Column(String(100),nullable=False)
    vehicle_classs = Column(String(100),nullable=False)
    manufacturer = Column(String(100),nullable=False)
    lenght = Column(String(100),nullable=False)
    cost_in_credits = Column(String(100),nullable=False)
    crew = Column(String(100),nullable=False)
    max_atmosphering_speed = Column(String(100),nullable=False)
    cargo_capacity = Column(String(100),nullable=False)
    consumables = Column(String(100),nullable=False)
    url = Column(String(200),nullable=False)
    created = Column(String(100),nullable=False)
    edited = Column(String(100),nullable=False)
    favorite = relationship('Favorite',backref='vehicle',lazy=True)

class People(Base):
    __tablename__ = 'people'
    peopleID = Column(Integer,primary_key=True)
    name = Column(String(100),nullable=False)
    birth_year = Column(String(100),nullable=False)
    eye_color = Column(String(100),nullable=False)
    gender = Column(String(100),nullable=False)
    hair_color = Column(String(100),nullable=False)
    height = Column(String(20),nullable=False)
    mass = Column(String(40),nullable=False)
    skin_color = Column(String(20),nullable=False)
    homeworld = Column(String(40),nullable=False)
    url = Column(String(100),nullable=False)
    created = Column(String(100),nullable=False)
    edited = Column(String(40),nullable=False)
    favorite = relationship('Favorite', backref='people',lazy=True)

class Favorite(Base):
    __tablename__ = 'favorite'
    favoriteID = Column(Integer,primary_key=True)
    people_id = Column(Integer,ForeignKey('people.peopleID'))
    vehicle_id = Column(Integer,ForeignKey('vehicle.vehicleID'))
    planet_id = Column(Integer,ForeignKey('planet.planetID'))
    usuario_id = Column(Integer,ForeignKey('usuario.usuarioID'))



       
    

""" class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}
 """
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
