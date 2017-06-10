# README - Udacity Project: Logs Analysis Project



The **Logs Analysis Project** is the third of several projects within the **Full Stack Web Developer Nanodegree** offered by **_Udacity_**.  This project is to simulate an **internal reporting tool** that will query information from the **news** database to answer three questions:

* What are the most popular three articles of all time?
* Who are the most popular authors of all time?
* On which days did more than 1% of the requests lead to errors?

This README assumes that you have already setup the **virtual machine** with **_VirtualBox_** and **_Vagrant_**, and you have configured the **VM** with the files provided by **_Udacity_**.

## Table of Contents

* Usage
  * Views - manually or `prepare_views.py`
  * Answers - `log_analyzer.py`
  * Cleanup - manually or `cleanup_db.py`
* Authors
* Acknowledgments

## Usage

**Views**

I created six views in the database to help answer the questions.  You can either set them up manually or automatically with the instructions below:

**_Manually_**

1. Connect to the **_news_** database
```
psql news
```
2. Create a view copy of **_log_** table that can be updated to remove '/article/' from the rows in **_path_** column.
```
CREATE VIEW cleanlog AS SELECT path, ip, method, status, time, id FROM log;
```
3. Make the update to the **_path_** column in **_cleanlog_** view to remove '/article/' from the string. 
```
UPDATE cleanlog SET path = replace(path, '/article/', '');
```
4. Create a view named **_articles1_** that joins **_articles_** and **_authors_**.
```
CREATE VIEW articles1 AS SELECT name, title, slug FROM articles JOIN authors ON articles.author = authors.id;
```
5. Create a view named **_popular_** that counts successful views of articles from **_cleanlog_**.
```
CREATE VIEW popular AS SELECT COUNT(path) as views, path FROM cleanlog WHERE status LIKE '%200%' AND path != '/' GROUP BY path ORDER BY views DESC;
```
6. Create a view named **_notfound_** that counts errors per day from **_cleanlog_**.
```
CREATE VIEW notfound AS SELECT time::date as day, status, count(id) as errors FROM cleanlog WHERE status = '404 NOT FOUND' GROUP BY day, status ORDER BY day;
```
7. Create a view named **_hits_** that counts the total site hits per day from **_cleanlog_**.
```
CREATE VIEW hits AS SELECT time::date as day, count(id) as hits FROM cleanlog GROUP BY day ORDER BY day;
```
8. Create a view named **_error_days_** that gets a raw percentage of errors per day from **_notfound_** and **_hits_**.
```
CREATE VIEW error_days AS SELECT notfound.day, errors/hits::float*100 AS percent FROM notfound JOIN hits ON notfound.day = hits.day GROUP BY notfound.day, notfound.errors, hits.hits ORDER BY notfound.day;
```
9. You can now answer the questions.  Skip to **_Answers_** section below.

**_Automatically_**

1. Run the `prepare_views.py` file.
```
python3 prepare_views.py
```
2. That's all there was to that!

****

**Answers**

1. Run the `log_analyzer.py` file.
```
python3 log_analyzer.py
```
2. These are the results that I get...
```
vagrant@vagrant:/vagrant$ python3 log_analyzer.py

Running queries, please wit...

The top 3 articles of all time are...

* Candidate is jerk, alleges rival - 338647 views
* Bears love berries, alleges bear - 253801 views
* Bad things gone, say good people - 170098 views
-----------------------------------------------------

The most popular authors of all time are...

* Ursula La Multa - 507594 views
* Rudolf von Treppenwitz - 423457 views
* Anonymous Contributor - 170098 views
* Markoff Chaney - 84557 views
-----------------------------------------------------

The following days experienced more than 1% errors...

* 2016-07-17 - 2.3 %
-----------------------------------------------------

Finished analyzing logs. You can now run cleanup_db.py.

vagrant@vagrant:/vagrant$ 
```
****

**Cleanup**

To restore the **_news_** database on the **VM**, you will need to perform a couple of `DROP VIEW` queries.  Once again, you can manually do it or have it done automaically.

**_Manually_**

1. Drop the **_cleanlog_** and the other views that it cascades down to.
```
DROP VIEW cleanlog CASCADE;
```
2. Drop the **_articles1_** view.
```
DROP VIEW articles1;
```
3. Close the connection to the news database.
```
\q
```

**_Automatically_**

1. Run the `cleanup_db.py` file.
```
python3 cleanup_db.py
```
2. That's all there was to that!

## Authors

* **Sean Magrann** - AT&T Services, Inc. | Emerging Technologies

## Acknowledgements

* [Udacity](https://www.udacity.com/) - Programming Foundations with Python
* [Udacity](https://www.udacity.com/) - The Backend: Databases & Applications



