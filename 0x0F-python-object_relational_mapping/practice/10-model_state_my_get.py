#!/usr/bin/python3
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__" :
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    arg = argv[4]

    fin = False
    for state in session.query(State):
        if state.name == arg:
            print("{}".format(state.id))
            fin = True
            break
    if fin is False:
        print("not here")
