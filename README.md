# Getting Started with Flask-URL-Shortener

## Technologies explanation
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) - main library.

**Note:** all packages can be restored from the **requirements.txt**

## Files structure explanation
1. **static** directory contains all static files such as files for styles or .js files;
2. **templates** directory contains html templates for our pages;
    1. base.html -> root structure;
    2. index.html -> main page that convert any url to short format;
    3. info.html -> page that represent all records in database table;
   4. get.url.html -> page return full url by uid of this url;
  
3. **__init__.py** configuration file;
4. **app.py** our main app file(This file will run).
5. **models.py** represent our db table structure.


## Get started
1. You should create your db with PosgreSQL;
2. Fill ```.env``` file with info about db port, name, password, user;
Example:
```
DB=mydb
PORT=5432
PASS=mypass
USER=whoami
```
3. Run command:
```
pip install requirements.txt
```
This command all the required packages;

4. Run in your terminal:
```python app.py```
Open [http://localhost:5000](http://localhost:5000) to view it in the browser.
