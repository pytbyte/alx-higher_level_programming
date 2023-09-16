#!/usr/bin/python3
"""7-model_states
python database manipulation program
uses Sqlalchemy and some base model
to query and display the entry of
table States in database hbtn_0e_6_usa
from argv passed.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

"""_summary_
1. handle argv for db connections and error reporting
2. try create engine and connect
3. create session
3.1. get argv with the query parameter (city name)
4. Query data and filter_by argv.
5. print formated data or throw error message on failiure
6. close session
"""

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("./10-m..<username><pswd> <db_name> <city>")
        sys.exit(1)

    name, pwd, db, city = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(name, pwd, db),
                               pool_pre_ping=True)

        Session = sessionmaker(bind=engine)
        db = Session()

        state_data = db.query(State).filter_by(name=city).first()

        if state_data:
            print("{}: {}".format(state_data.id, state_data.name))
        else:
            print("Not found")

    except Exception as e:
        print("something went wrong: ", e)

    finally:
        db.close()
