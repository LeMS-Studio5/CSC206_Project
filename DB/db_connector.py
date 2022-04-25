import os
import configparser
from random import random
from unicodedata import name
from sqlalchemy import Float, create_engine, func
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, select
from sqlalchemy.orm import sessionmaker, relationship

# configparser is part of Python and will read configuration setttings in a 
# variety of formats. https://docs.python.org/3/library/configparser.html
# This file is where you would store usernames and passwords AND you DON'T
# upload the config file to GitHub.
# config = configparser.ConfigParser()
# config.read('settings.conf')

# # Engine is the core interface to the database
# dbconnect = config["MYSQL"]["SQLALCHEMY_DATABASE_URI"]
# engine = create_engine(dbconnect, echo=True)
# Base class for declaring tables
Base = declarative_base()
class Athlete(Base):
    __tablename__ = 'athletes'
    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    nationality = Column(String(45), nullable=False)
    currentrank = Column(Integer, nullable=False)
    prevyearrank = Column(Integer,nullable=True)
    sport = Column(String(45), nullable=False)
    year = Column(Integer, nullable=False)
    earnings = Column(Float, nullable=False)

    def __repr__(self):
        return "<Athlete(Name='%s', Nation='%s', Current Rank='%s', Previous Rank='%s', Sport='%s', Year='%s', Earnings='%s')>" % (self.name, self.nationality, self.currentrank, self.prevyearrank, self.sport, self.year, self.earnings)


class DbConnector:   

    def __init__(self, createTable):
        
        self.config = configparser.ConfigParser()
        self.config.read('setting.conf')

        # Engine is the core interface to the database
        # print(self.config['DEFAULT']['ServerAliveInterval'])
        dbconnect = self.config["MYSQL"]["SQLALCHEMY_DATABASE_URI"]
        engine = create_engine(dbconnect, echo=True)
        # Create a databsae session, bind to the engine and prepare to use
        Session = sessionmaker()
        Session.configure(bind=engine)
        self.session = Session()
        if (createTable==True):
# Create the tables in the database
            Base.metadata.create_all(engine)

    def Session(self):
        return self.session
    def con(self):
        engine = create_engine(self.config["MYSQL"]["SQLALCHEMY_DATABASE_URI"])
        return engine.connect()
    def allContent(self):

        #Equivalent to 'SELECT * FROM census'
        query = select(Athlete) 

        ResultProxy = self.con().execute(query)

        return ResultProxy.fetchall()
    def nationContent(self,nation):

        #Equivalent to 'SELECT * FROM census'
        query = select(Athlete).where(Athlete.nationality==nation)

        ResultProxy = self.con().execute(query)

        return ResultProxy.fetchall()
    def newerThanContent(self,year):

        #Equivalent to 'SELECT * FROM census'
        query = select(Athlete).where(Athlete.year>year)

        ResultProxy = self.con().execute(query)

        return ResultProxy.fetchall()