#!/usr/bin/python3
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__" :
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for i in session.query(State, City).filter(State.id == City.state_id):
        print("{}: ({:d}) {}".format(i.State.name, i.City.id, i.City.name))

