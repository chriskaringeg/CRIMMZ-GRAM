# CRIMMZ-GRAM

## Author

KARINGE KINYUA

## Description

A clone of the popular photo-sharing site Instagram

## User Stories 
- Sign in to the application to start using.
- Upload my pictures to the application.
- See my profile with all my pictures.
- Follow other users and see their pictures on my timeline.
- Like a picture and leave a comment on it.
- How to use 
When the user opens the website, he/she will see the will be prompted to sign up or sign in.The user will be able to see posts that other users have posted. He/she can also add their own posts. A user can follow other users and view images posted by those users The user also has a personalized profile where they can edit their profile and view the photos they have postd

## Technologies used 
- HTML and CSS
- Python
- Django
- Postgres
- Heroku for deployment

## Set up and Installation

###  Prerequisites
The user will require git, django, postgres and python3.6+ installed in their machine. To install these two, you can use the following commands

#git
$ sudo apt install git-all

#python3.6
$ sudo apt-get install python3.6.

#django
$ pip install django==1.11

#postgres
$ sudo apt-get install postgresql postgresql-contrib libpq-dev

## Requirements

-bootstrap4==0.1.0
config==0.4.0
confusable-homoglyphs==3.2.0
dj-database-url==0.5.0
Django==1.11
django-bootstrap4==0.0.7
django-crispy-forms==1.7.2
django-heroku==0.3.1
django-registration==2.4.1
django-tinymce==2.8.0
gunicorn==19.9.0
Pillow==5.4.1
psycopg2==2.7.7
python-decouple==3.1
pytz==2018.9
whitenoise==3.3.1


## .ENV file
SECRET_KEY='<SECRET_KEY>'
DEBUG=True #set to false in production
DB_NAME='tribune'
DB_USER='user'
DB_PASSWORD='password'
DB_HOST='127.0.0.1'
MODE='dev' #set to 'prod' in production
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
DISABLE_COLLECTSTATIC=1

## Installation
- To access this application on your command line, you need to clone it git clone https://github.com/chriskaringeg/CRIMMZ-GRAM.git
- Create a requirements.txt in the root folder and copy the requirements above.
- Install the required technologies with pip install -r requirements.txt
- Create a .env file and copy the .env code above
- You can then run the server with: python3.6 manage.py runserver
- You can make changes to the db with python3.6 manage.py makemigrations photos python3.6 manage.py migrate

## License

MIT

Copyright (c) {2019} **{KARINGE KINYUA}**

