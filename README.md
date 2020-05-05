# FSND-Capstone-Project
Udacity Fullstack Nanodegree capstone project

https://fsnd-happyhour.herokuapp.com/
 
The motivation of this project is to practice the skills learned during the Udacity FullStack NanoDegree program. The basis of the app for restaurant managers to be able to post their restraurant and menus for customers to be able to see and make reservations.  

# The Stack
    * Python
    * Flask
    * SQLAlechmy
    * Postgres Database
    * Flask - Migrate
    * JSON Web Token (JWT) - Auth0 (auth0.com)
    * Python virtual environment

# Requirements
1. Install the necessary requirmenets by running:

``` bash
pip install -r requirements.txt
```
2. Open a terminal and cd to the project directory:
``` bash
cd ~/FSND-Capstone-Project
```
3. Set up your DATABASE_URL variable depending on OS:

``` bash
export DATABASE_URL="{DATABASE_URL}"

For Windows use:

$env:DATABASE_URL="{DATABASE_URL}"
```

4. Run ALL three migration commands ONLY on you first set up:

``` bash
# Run the init command once
python manage.py db init
python manage.py db migrate
python manage.py db upgrade

# Run the last 2 commands if/when you make changes to database structure
```

5. Set up FLASK_APP variable depending on OS:
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

 
# Credits

Created by Viktor Dojnov - https://github.com/vdojnov

Special thanks to Kurt Galvin - https://github.com/kurtgalvin






