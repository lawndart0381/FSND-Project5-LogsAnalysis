#!/usr/bin/env python3
import time
import psycopg2

dbname = "news"

# Connect to news database
db = psycopg2.connect(database=dbname)
c = db.cursor()
print()

# Display the TOP 3 articles of all time sorted by most to least
query = 'SELECT title, views '\
        'FROM articles1 '\
        'JOIN popular '\
        'ON slug = path '\
        'LIMIT 3'
c.execute(query)
top3 = c.fetchall()
print("The top 3 articles of all time are...")
print()
for row in top3:
    time.sleep(0.3)
    print("*", row[0], "-", row[1], "views")
print("-----------------------------------------------------")
print()

# Display the most popular authors sorted by most views to least
query = 'SELECT name, SUM(views) as views '\
        'FROM articles1 '\
        'JOIN popular '\
        'ON slug = path '\
        'GROUP BY name '\
        'ORDER BY views DESC'
c.execute(query)
popular = c.fetchall()
print("The most popular authors of all time are...")
print()
for row in popular:
    time.sleep(0.3)
    print("*", row[0], "-", row[1], "views")
print("-----------------------------------------------------")
print()

# Display the days with errors greater than 1%
query = 'SELECT day, ROUND(CAST (percent AS numeric),1) AS percent '\
        'FROM error_days '\
        'WHERE percent > 1 '\
        'ORDER BY day'
c.execute(query)
errordays = c.fetchall()
print("The following days experienced more than 1% errors...")
print()
for row in errordays:
    time.sleep(0.3)
    print("*", row[0], "-", row[1], "%")
print("-----------------------------------------------------")
print()
db.close()
