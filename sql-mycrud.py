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


# create a class-based model for the "Writter" table
# class Writter(base):
#     __tablename__ = "Writter"
#     id = Column(Integer, primary_key=True)
#     first_name = Column(String)
#     last_name = Column(String)
#     country_name = Column(String)
#     favorite_book = Column(String)
#     age = Column(Integer)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# creating records on our Place table
# leon = Place(
#     country_name="Nicaragua",
#     capital_name="Managua",
#     language="Spanish"
# )

dubai = Place(
    country_name="UAE",
    capital_name="Abudabi",
    language="Arab"
)


# creating records on our Writter table
# kate_morton = Writter(
#     first_name="Kate",
#     last_name="Morton",
#     country_name="Australia",
#     favorite_book="The secret garden",
#     age=47
# )

# paulo_coelho = Writter(
#     first_name="Paulo",
#     last_name="Coelho",
#     country_name="Brazil",
#     favorite_book="The alchemyst",
#     age=75
# )

# ken_follet = Writter(
#     first_name="Ken",
#     last_name="Follet",
#     country_name="British",
#     favorite_book="The pillars of the earth",
#     age=73
# )

# add each instance of our places to our session
# session.add(leon)
session.add(dubai)
# session.add(kate_morton)
# session.add(paulo_coelho)
# session.add(ken_follet)


# updating a single record
# writter = session.query(Writter).filter_by(id=1).first()
# writter.age=47
# writter.favorite_book="The distant hours"


# commit our session to the database
session.commit()


# deleting a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# writter = session.query(Writter).filter_by(first_name=fname,
#                                                last_name=lname).first()
# defensing programming
# if writter is not None:
#     print("Writter found: ", writter.first_name + " "
#           + writter.last_name)
#     confirmation = input("Are you sure you want to delete this record?(y/n)")
#     if confirmation.lower() == "y":
#         session.delete(writter)
#         session.commit()
#         print("Writter has been deleted")
#     else:
#         print("Writter not deleted")
# else:
#     print("No records found")


# delete multiple/all records
# places = session.query(Place)
# for place in places:
#     session.delete(place)
#     session.commit()

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

# query the database to find all writters
# writters = session.query(Writter)
# for writter in writters:
#     print(
#         writter.id,
#         writter.first_name,
#         writter.last_name,
#         writter.country_name,
#         writter.favorite_book,
#         writter.age,
#         sep=" | "
#     )
