#!/usr/bin/python3
"""
Creates a new State "California"
and associates it with a City "San Francisco"
in a MySQL database.
Usage: python3 script.py <username> <password> <database>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base as StateBase, State
from relationship_city import City

"""
Create the database engine
Create tables for State and City
Create a new City object
Create a new State object and associate it with the City
Add the State and City objects to the session and commit
"""

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 script.py <username> <password> <database>")
    else:
        user, pwd, db = sys.argv[1], sys.argv[2], sys.argv[3]
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(user, pwd, db),
                               pool_pre_ping=True)

        StateBase.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        db_session = Session()

        try:

            new_city = City(name="San Francisco")

            new_state = State(name="California", cities=[new_city])

            db_session.add(new_state)
            db_session.commit()
            print("State 'California' with City'San Francisco' created .")

        except Exception as e:
            print(f"An error occurred: {e}")
            db_session.rollback()
        finally:
            db_session.close()
