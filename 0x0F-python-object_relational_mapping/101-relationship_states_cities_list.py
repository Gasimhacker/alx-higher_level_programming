#!/usr/bin/python3

"""
A script that lists all State objects,
and corresponding City objects,
contained in the database hbtn_0e_101_usa
Format:
    <state id>: <state name>
    <tabulation><city id>: <city name>
"""


if __name__ == "__main__":
    from sys import argv
    from relationship_city import City, Base
    from relationship_state import State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    db_url = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'

    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    q = session.query(State).order_by(State.id).all()

    for state in q:
        print(f"{state.id}: {state.name}")
        [print(f"\t{city.id}: {city.name}") for city in state.cities]
