#!/usr/bin/python3
""" This script lists all State objects Louisiana
to the database hbtn_0e_6_usa """

if __name__ == "__main__":

    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    session = Session(engine)

    new_value = State(name='Louisiana')
    session.add(new_value)
    session.commit()

    states = session.query(State).filter(State.name == 'Louisiana').first()

    print(states.id)
