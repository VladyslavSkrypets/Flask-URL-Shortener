# Getting Started with Flask-URL-Shortener

**Note:** all packages can be restored from the **requirements.txt**

## Task

Reduce long URLs to short ones without losing value. This gives the link better readability for the user.
Example:
```
Long url: https://ua.jooble.org/%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0-junior-python/%D0%9A%D0%B8%D0%B5%D0%B2
Short url: https://bit.ly/30Pjyul
```

## Functional explanation
1. ```Path /```
Select the link you want to shorten and choose its lifetime (for how many days the link will be active. Default 90 days).
At the end of the confirmation, a short link will be generated that will redirect you to the required address.

![start](https://user-images.githubusercontent.com/77641899/135723904-6d52cf2f-253e-43cb-8bda-5b9e293f5cf8.png)

**Note:** After the link expires, it will be inaccessible !


2. ```Path /get_url```
Each short link has its own uid (8 characters after /). Knowing the uid, you can find the original length link.

![second](https://user-images.githubusercontent.com/77641899/135724046-0256c0e9-e8f6-420c-b384-4107303edc40.png)

3. ```Path /all_info```
On this page you can see all the information about the saved links.

![third](https://user-images.githubusercontent.com/77641899/135724128-88739d5c-ea74-4b8c-803e-2955c51a9700.png)


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
This command install all the required packages;

4. Run in your terminal:
```python app.py```
Open [http://localhost:5000](http://localhost:5000) to view it in the browser.

## API

Read about interaction with api [here]()
