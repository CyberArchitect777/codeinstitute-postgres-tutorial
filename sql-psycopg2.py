import psycopg2

# connect to "chinook" database

connection = psycopg2.connect(database="chinook")

# build a cursor object of the database

cursor = connection.cursor()

# CI Query 1 - select all records from the "Artist" table

#cursor.execute('SELECT * FROM "Artist"')

# CI Query 2 - select only the "Name" column from the "Artist" table

#cursor.execute('SELECT "Name" FROM "Artist"')

# CI Query 3 - select only "Queen" from the "Artist" table

#cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# CI Query 4 - Select only by "ArtistId" #51 from the "Artist" table

#cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# CI Query 5 - select only the albums with "ArtistId" #51 on the "Album" table

#cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# CI Query 6 - select all tracks where the composer is "Queen" from the "Track" table

#cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# Queries - Challenges

# This method is not recommended due to SQL injection attacks
#cursor.execute('SELECT * FROM "Artist" WHERE "Name" = \'Aerosmith\'')

# SQL injection safe approach
#cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Aerosmith"])

# Missing artist search (returns nothing)
#cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Aero2smith"])

# Multiple criteria search in an SQL injection safe way

cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s AND "Name" = %s', [3, "Aerosmith"])

# fetch the results (multiple)

results = cursor.fetchall()

# fetch the results (single)

#results = cursor.fetchone()

# close the connection

connection.close()

# print results

for result in results:
    print(result)

