#!/usr/bin/python3
"""7-model_states
python database manipulation program
uses Sqlalchemy and some base model
to add a new entry of city "Louisiana" to
table States in database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

"""_summary_
1. handle argv for db connections and error reporting
2. try create engine and connect
3. create session
4. Insert new data into the table.
5. print formated data or throw error message on failiure
6. close session
"""

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("./11-m..<username><pswd> <db_name>")
        sys.exit(1)

    name, pwd, db = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(name, pwd, db),
                               pool_pre_ping=True)

        Session = sessionmaker(bind=engine)
        db = Session()

        new_entry = State(name="Louisiana")
        db.add(new_entry)
        db.commit()

        print("{}".format(new_entry.id))

    except Exception as e:
        print("something went wrong: ", e)

    finally:
        db.close()
