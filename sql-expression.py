from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer,
    String, MetaData
)

# executing the instructions from our localhost chinook database
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# create variable for artist table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# create variable for album table
album_table = Table(
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# create variable for tracks table
track_table = Table(
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", String, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# making the connection:
with db.connect() as connection:
    # Query 1 - select all the records from artist_table
    select_query = artist_table.select()

    results = connection.execute(select_query)
    for result in results:
        print(result)
