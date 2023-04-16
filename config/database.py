# Libraries
import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Storaging Database Name
sqlite_file_name = "../database.sqlite"
# Reading Database
base_dir = os.path.dirname(os.path.realpath(__file__))

# Getting Join Method to set DataBase Connection
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

# DataBase Engine
engine = create_engine(database_url, echo=True)

#Session connector to DataBase
Session = sessionmaker(bind=engine)

# DataBase Table Manipulation
Base = declarative_base()
