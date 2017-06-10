#!/usr/bin/env python3
import os
import time
import psycopg2

dbname = "news"

# Connect to news and create some views for log_analyzer.py
db = psycopg2.connect(database=dbname)
c = db.cursor()

# Create a cleaner view of log (view = cleanlog)
query = "CREATE VIEW cleanlog AS SELECT * FROM log;"
c.execute(query)
print()
print(c.statusmessage, "'cleanlog'")
db.commit()
time.sleep(0.5)
query = "UPDATE cleanlog SET path = REPLACE(path, '/article/', '');"
print("Updating cleanlog, please wait...")
c.execute(query)
print(c.statusmessage, "rows to remove '/article/' from the path string")
db.commit()
time.sleep(0.5)

# Create articles1 view that joins articles and authors
query = 'CREATE VIEW articles1 AS SELECT name, title, slug '\
        'FROM articles JOIN authors ON articles.author = authors.id;'
c.execute(query)
print(c.statusmessage, "'articles1'")
db.commit()
time.sleep(0.5)

# Create popular view that counts successful views of articles from cleanlog
query = 'CREATE VIEW popular AS SELECT COUNT(path) as views, path '\
        'FROM cleanlog WHERE status = %s AND path != %s '\
        'GROUP BY path ORDER BY views DESC;'
conditions = ("200 OK", "/")
c.execute(query, conditions)
print(c.statusmessage, "'popular'")
db.commit()
time.sleep(0.5)

# Create notfound view that counts errors per day from cleanlog
query = 'CREATE VIEW notfound AS '\
        'SELECT time::date AS day, status, COUNT(id) as errors '\
        'FROM cleanlog WHERE status = %s '\
        'GROUP BY day, status ORDER BY day;'
condition = ("404 NOT FOUND",)
c.execute(query, condition)
print(c.statusmessage, "'notfound'")
db.commit()
time.sleep(0.5)

# Create hits view that counts total site hits per day
query = 'CREATE VIEW hits AS '\
        'SELECT time::date as day, count(id) as hits '\
        'FROM cleanlog '\
        'GROUP BY day ORDER BY day;'
c.execute(query)
print(c.statusmessage, "'hits'")
db.commit()
time.sleep(0.5)

# Create error_days view that gets raw percentage of errors per day
query = 'CREATE VIEW error_days AS '\
        'SELECT notfound.day, errors/hits::float*100 AS percent '\
        'FROM notfound JOIN hits ON notfound.day = hits.day '\
        'GROUP BY notfound.day, notfound.errors, hits.hits '\
        'ORDER BY notfound.day;'
c.execute(query)
print(c.statusmessage, "'error_days'")
db.commit()
time.sleep(0.5)
print()
print("You can now run log_analyzer.py!")
print()

db.close()
