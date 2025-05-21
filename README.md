# RockClimbs App :muscle:
## A website as part of the Web Services and Applications course

This github repository helps you set your own database of climbs as well as deploying it in a web interface where you can perform crud operations. 

It is also deployed in pythonanywhere in the following url https://gfmg.pythonanywhere.com/, which you can have a look to see the current interface. At the moment,  the App allows to view your current climbs, add new climbs and also view the crags added in the database, but I will continue building functionalities to it, and I welcome you to do it too! 

## Repository structure
The repository contains the following folder and files: 

- **climbDao.py**: handles all direct interactions with the MySQL database, functions to insert rows, delete climbs, view climbs etc etc...
- **server.py**:  is the main web server. It defines your routes, serves HTML pages, and handles AJAX/API requests.
- **Templates folder**: the templates folder contains the .html files that are displayed in the web app. 
- **rockclimbs.sql**: this sql file helps you set the database of your climbs locally, so you can use the remaining of the scripts within this repository to test the App and continue modifying it. Simply copy it , include your climbs, crags or any other information you might want to store and create the database locally using MySQL. 
- **dbconfig.py**: This code defines a Python dictionary that stores the configuration details required to connect to a MySQL database. It is then used with MySQL client libraries (mysql.connector) to establish a database connection in the python application (working to set it up with python/anywhere currently).

