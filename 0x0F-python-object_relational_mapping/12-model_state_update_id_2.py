#!/usr/bin/python3
"""12-model_state_update_id_2
python database manipulation program
uses Sqlalchemy and some base model
to update an entry where id=2 in
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
4. fetch city entry object data where id=2
4.1. update city name and save
5. print formated data or throw error message on failiure
   and roll back to previous data object.
6. close session
"""

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("./12-m..<username><pswd> <db_name>")
        sys.exit(1)

    name, pwd, db = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(name, pwd, db),
                               pool_pre_ping=True)

        Session = sessionmaker(bind=engine)
        db = Session()

        Target_entry = db.query(State).filter_by(id=2).first()
        Target_entry.name = "New Mexico"
        db.commit()

    except Exception as e:
        db.rollback()
        print("something went wrong: ", e)

    finally:
        db.close()
