#!/usr/bin/python3
"""7-model_states
python database manipulation program
uses Sqlalchemy and some base model
to query and display all contents of
table States in database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

"""_summary_
1. handle argv for db connections and error reporting
2. try create engine and connect
3. create session
4. Query data
5. print formated data or throw error message on failiure
6. close session
"""

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("./7-modal_states.py <username> <password> <database_name>")
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(username, password, db_name),
                               pool_pre_ping=True)

        Session = sessionmaker(bind=engine)
        db = Session()

        states_data = db.query(State).order_by(State.id).all()

        for state in states_data:
            print("{}: {}".format(state.id, state.name))

    except Exception as e:
        print("something went wrong: ", e)
    finally:
        db.close()
