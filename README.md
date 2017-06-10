# README - Udacity Project: Logs Analysis Project
****


The **Logs Analysis Project** is the third of several projects within the **Full Stack Web Developer Nanodegree** offered by **_Udacity_**.  This project is to simulate an **internal reporting tool** that will query information from the **news** database to answer three questions:
* What are the most popular three articles of all time?
* Who are the most popular authors of all time?
* On which days did more than 1% of the requests lead to errors?

This README assumes that you have already setup the **virtual machine** with **_VirtualBox_** and **_Vagrant_**, and you have configured the **VM** with the files provided by **_Udacity_**.
## Table of Contents
****
* Installation
  * Python2.7
  * FTMT.zip
* Usage
  * IDLE (_Python GUI_)
  * Run `entertainment_center.py`
  * Edit `entertainment_center.py` (_Optional_)
* Authors
* Acknowledgments

## Installation
****
#### Python 2.7
In order to run this `code`, you will need to install **_Python 2.7.13_** on your machine.  You can download Python from the [**Official Website**](https://www.python.org/downloads/).

* [Windows Installation Instructions](http://docs.python-guide.org/en/latest/starting/install/win/)
* [Mac OSX Installation Instructions](http://docs.python-guide.org/en/latest/starting/install/osx/)

#### FTMT.zip
The fact that you're reading this README file means that you have already extracted the files in **_FTMT.zip_** with an extraction tool of your liking.  In order to view the **Fresh Tomatoes Movie Trailers** webpage, you will need to ensure the `media.py`, `entertainment_center.py`, and `fresh_tomatoes.py` files are contained in the same directory folder of your liking.

## Usage
****
The easiest way to run this program is through **IDLE**, which was installed during the **Python** installation.
* [Windows IDLE Instructions](https://hkn.eecs.berkeley.edu/~dyoo/python/idle_intro/index.html)
* [Mac IDLE Instructions](http://homepages.cwi.nl/~jack/macpython_help/ide/)

### Running the `code`
Once you have opened **IDLE**, select _File_ then _Open_.
![alt text](https://dl.dropboxusercontent.com/u/29108866/MarkdownImages/IDLE_file_open.png)

Browse to the directory folder where `media.py`, `entertainment_center.py`, and `fresh_tomatoes.py` files are contained, and select `entertainment_center.py` to open the module.
![alt text](https://dl.dropboxusercontent.com/u/29108866/MarkdownImages/IDLE_browse_to_file.png)

![alt text](https://dl.dropboxusercontent.com/u/29108866/MarkdownImages/entertainment_center.png)

To run the module, select _Run_ and then _Run Module_.  Or you can simply hit _F5_.
![alt text](https://dl.dropboxusercontent.com/u/29108866/MarkdownImages/run_module.png)

**Success!**  You are now viewing the webpage of _my favorite_ movie trailers!  You can click on the movie poster tiles to watch the **_YouTube_** trailers.
**Warning!** Some of the movie trailers that are rated **R** may contain language that is offensive and/or not suitable for young children.
![alt text](https://dl.dropboxusercontent.com/u/29108866/MarkdownImages/web_page.png)
   
### Editing the `code`

It is recommended that you have a working knowledge of _Object Oriented Programming_ **(Python)**.  There is no need to edit anything in `media.py` or `fresh_tomatoes.py`.

To personalize the page with your own favorite movies, you will edit the data objects in `entertainment_center.py`.
There are five elements that will need edited for each movie object:
1. The object name (Ex. Movie = Toy Story, change `some_movie = media.Movie` to `toy_story = media.Movie`) 
2. Movie Title
3. A URL to your movie's poster image
4. A URL to your movie's rating image
5. A URL to your movie's trailer

#### Example Code for Movie Objects
```python
# Movie data for Fresh Tomatoes Movie Trailers
some_movie = media.Movie("Some Movie", # Your movie's title
                        "http://someurl.com", # Link to your movie's poster image
                        "http://someurl.com", # Link to your movie's rating image
                        "http://someurl.com") # Link to your movie's trailer
```

Once you have personalized your movie objects, you will need to edit the list of object names that will be opened in `fresh_tomatoes.py`.  The list is located near the bottom of `entertainment_center.py` below the comment `# List of movies for create_movie_tiles_content function in fresh_tomatoes`. 
#### Example Code for Movie List
```python
# List of movies for create_movie_tiles_content function in fresh_tomatoes   
movies = [some_movie, toy_story] # To create a list, use a comma between object name entries
```
Save your edits to `entertainment_center.py`, and hit _F5_ to see your new page!  Good Luck!
## Authors
****
* **Sean Magrann**

## Acknowledgements
****
* [UDACITY](https://www.udacity.com/) - Programming Foundations with Python



