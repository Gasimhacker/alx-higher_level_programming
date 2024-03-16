#!/usr/bin/python3

"""
A script that lists all State objects from the database hbtn_0e_6_usa
"""


if __name__ == "__main__":
    from sys import argv
    from model_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    db_url = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'

    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    session = Session()

    query = session.query(State).order_by(State.id)

    for state in query.all():
        print(f"{state.id}: {state.name}")
