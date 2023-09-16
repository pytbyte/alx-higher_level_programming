#!/usr/bin/python3
"""7-model_states
python database manipulation program
uses Sqlalchemy and some base model
to query and display the entry that
contains letter "a" in
table States in database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker

"""_summary_
1. handle argv for db connections and error reporting
2. try create engine and connect
3. create session
4. Query data and filter_by column entry with "a" in name.
5. print formated data or throw error message on failiure
6. close session
"""

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("./8-modal.. <username><password> <database_name>")
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(username, password, db_name),
                               pool_pre_ping=True)

        Session = sessionmaker(bind=engine)
        db = Session()

        states_data = db.query(State).all()
        for state in states_data:
            if "a" in state.name:
                print("{}: {}".format(state.id, state.name))

    except Exception as e:
        print("something went wrong: ", e)

    finally:
        db.close()
