# FSND-Capstone-Project
Udacity Fullstack Nanodegree capstone project

https://fsnd-happyhour.herokuapp.com/
 
The motivation of this project is to practice the skills learned during the Udacity FullStack NanoDegree program. The basis of the app for restaurant managers to be able to post their restraurant and menus for customers to be able to see and make reservations.  

* Link to course click [here](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd0044)

* Link to course syllabus, click [here](https://bertelsmann-university.com/fileadmin/user_upload/Full_Stack_ND_Syllabus.pdf) 

# The Stack
* [Python 3.8.2](https://www.python.org/downloads/release/python-382/)  
* [Flask - Web Framework](https://flask.palletsprojects.com/en/1.1.x/)
* [SQLAlechmy ORM](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
* [PostgresSQL 12.2](https://www.postgresql.org/docs/12/release-12-2.html) 
* [Flask - Migrate](https://flask-migrate.readthedocs.io/en/latest/)
* Authentication - JSON Web Token (JWT) with [Auth0](auth0.com)
* User Roles/Permissions
* Python virtual environment - [venv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
* API testing with [Postman](https://www.postman.com/)
* Deployment on [Heroku](https://heroku.com/)

# Getting Started
**Requirements**

Install the necessary requirmenets by running:

``` bash
pip install -r requirements.txt
```

**Running on local machine**
1. Open a terminal and cd to the project directory:
``` bash
cd ~/FSND-Capstone-Project
```
2. Set up your DATABASE_URL variable depending on OS:

``` bash
export DATABASE_URL="{DATABASE_URL}"

For Windows use:

$env:DATABASE_URL="{DATABASE_URL}"
```

3. Run ALL three migration commands **ONLY** on you first set up:

``` bash
# Run the init command once
python manage.py db init
python manage.py db migrate
python manage.py db upgrade

# Run the last 2 commands if/when you make changes to database structure
```

4. Set up FLASK_APP variable depending on OS:
``` bash
export FLASK_APP=app.py

For Windows use:

$env:FLASK_APP="app.py"
```

5. To run the app use:
``` bash
flask run
```
* By default, the app will run on http://127.0.0.1:5000/ 

# Authentication 
 * This app can be run at https://fsnd-happyhour.herokuapp.com/

 * You can securly Sign Up or Log In through Auth0: https://fsnd-happyhour.auth0.com/authorize?audience=fsndcapstone&response_type=token&client_id=rY3ee6xjoWocXP7PkCUouHS48vX9YAoo&redirect_uri=http://localhost:5000/login-results


# Testing
* Testing instructions
1. Create a new database for testing (choose and new name ex. _new_testing_db_)

        createdb new_testing_db

2. In **test_app.py** set _database_name_ and _database_path_ from your local machine

3. In the command line run
``` bash
python test_app.py
```
4. The tests will run and should all be completed sucessfully

# Deployment
* Deployment on Heroku instructions

# Authors
* **Viktor Dojnov** - https://github.com/vdojnov

# Acknowledgments
Special thanks to:
* Kurt Galvin - https://github.com/kurtgalvin
* The Udacity Team!
