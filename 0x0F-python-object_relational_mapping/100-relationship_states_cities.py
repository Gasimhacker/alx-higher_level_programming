#!/usr/bin/python3

"""
A script that creates the State “California”
with the City “San Francisco”
from the database hbtn_0e_100_usa
"""


if __name__ == "__main__":
    from sys import argv
    from relationship_city import City, Base
    from relationship_state import State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    db_url = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'

    engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
