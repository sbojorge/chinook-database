from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Place" table
class Place(base):
    __tablename__ = "Place"
    id = Column(Integer, primary_key=True)
    country_name = Column(String)
    capital_name = Column(String)
    language = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# creating records on our Place table
leon = Place(
    country_name="Nicaragua",
    capital_name="Managua",
    language="Spanish"
)

# add each instance of our places to our session
session.add(leon)

# commit our session to the database
session.commit()

# query the database to find all places
places = session.query(Place)
for place in places:
    print(
        place.id,
        place.country_name,
        place.capital_name,
        place.language,
        sep=" | "
    )
