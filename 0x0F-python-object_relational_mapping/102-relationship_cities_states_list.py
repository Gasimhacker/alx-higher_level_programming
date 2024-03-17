#!/usr/bin/python3

"""
A script that lists all City objects from the database hbtn_0e_101_usa
Format:
    <city id>: <city name> -> <state name>
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

    q = session.query(City).order_by(City.id).all()

    for city in q:
        print(f"{city.id}: {city.name} -> {city.state.name}")
