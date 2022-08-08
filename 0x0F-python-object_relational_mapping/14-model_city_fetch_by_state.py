#!/usr/bin/python3
""" This script lists all State objects with the name passed as
argument from database hbtn_0e_6_usa """

if __name__ == "__main__":

    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_city import City

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    session = Session(engine)
    for state, city in session.query(State, City)\
                              .filter(City.state_id == State.id)\
                              .order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
