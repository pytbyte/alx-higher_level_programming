#!/usr/bin/python3
"""14-model_city_fetch_by_state
python database manipulation program
uses Sqlalchemy and some base model
to query and display all City objects in database
hbtn_0e_14_usa.
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

"""_summary_
1. handle argv for db connections and error reporting
2. try create engine and connect
3. create session
4. Query Cityand state data and join each state with its cities
5. print formated data or throw error message on failiure
6. close session
"""

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("./10-m..<username><pswd> <db_name>")
        sys.exit(1)

    name, pwd, db = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(name, pwd, db),
                               pool_pre_ping=True)

        Session = sessionmaker(bind=engine)
        db = Session()

        states_city = db.query(City, State).join(State).order_by(City.id).all()
        for city, state in states_city:
            print("{}: ({}) {}".format(state.name, city.id, city.name))

    except Exception as e:
        print("something went wrong: ", e)

    finally:
        db.close()
