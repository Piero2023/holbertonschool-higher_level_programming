#!/usr/bin/python3
""" This script changes the name of a State object from
the database hbtn_0e_6_usa """

if __name__ == "__main__":

    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    session = Session(engine)
    states = session.query(State).filter(State.id == 2).first()

    states.name = 'New Mexico'
    session.commit()
