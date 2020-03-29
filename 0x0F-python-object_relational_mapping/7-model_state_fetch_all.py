#!/usr/bin/python3
"""
    Script that select all rows from states table using SQLAlchemy
"""

import sys
import json
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).order_by((State.id))

    for row in query.all():
        print("{}: {}".format(row.id, row.name))
