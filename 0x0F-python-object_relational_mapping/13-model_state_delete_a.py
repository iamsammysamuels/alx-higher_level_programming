#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter a from the database
"""
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    drop_states = session.query(State).filter(State.name.contains('a'))
    for state in drop_states:
        session.delete(state)
    session.commit()
    session.close()
