#!/usr/bin/env python3
import sys
import time
import psycopg2

dbname = "news"

# Connect to news to perform cleanup
db = psycopg2.connect(database=dbname)
c = db.cursor()

# Query the database to show current views
query = 'SELECT viewname FROM pg_catalog.pg_views '\
        'WHERE schemaname NOT IN (%s, %s)'
filters = ("pg_catalog", "information_schema")
c.execute(query, filters)
print()
time.sleep(0.5)
print("The following views from Sean Magrann exist in news...")
print()
time.sleep(0.3)
print(c.statusmessage)
views = c.fetchall()
for row in views:
    time.sleep(0.3)
    print("*", row[0])

print()

delete_views = input("Would you like to delete Sean's views? (y/N)")
print()
if delete_views in ['y', 'Y', 'yes', 'Yes', 'YES']:
    print("Deleting Sean's views from news...")
    print()
    # Queries to drop views
    query = 'DROP VIEW cleanlog CASCADE;'
    c.execute(query)
    time.sleep(0.5)
    print(c.statusmessage, "cleanlog and it's cascaded table views")
    db.commit()
    query = 'DROP VIEW articles1;'
    c.execute(query)
    time.sleep(0.5)
    print(c.statusmessage, "articles1")
    db.commit()
    print()
    # Query to validate views were dropped
    query = 'SELECT viewname FROM pg_catalog.pg_views '\
            'WHERE schemaname NOT IN (%s, %s)'
    filters = ("pg_catalog", "information_schema")
    c.execute(query, filters)
    time.sleep(0.5)
    print(c.fetchone(), "of the views that Sean created exist anymore!")
    print("You can check by running '$ psql news' then 'news=> \dv'")
    print()
    print(c.statusmessage)
    db.close()
    print()
else:
    print("You've chosen not to delete Sean's views, closing connection")
    db.close()
    print()
