# CRIMMZ-GRAM

## Author

KARINGE KINYUA

## Description
A personal clone of the popular photo-sharing site Instagram(desktop version)

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

- Django==1.11
- django-bootstrap3==11.0.0
- django-registration==2.4.1
- django-tinymce==2.8.0
- Pillow==6.0.0
- psycopg2==2.8.2
- python-decouple==3.1
- pytz==2019.1


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
- To access this application on your command line, you need to clone it git clone https://github.com/chriskaringeg/CRIMMZ-GRAM.git.git
- Create a requirements.txt in the root folder and copy the requirements above.
- Install the required technologies with pip install -r requirements.txt
- Create a .env file and copy the .env code above
- You can then run the server with: python3.6 manage.py runserver
- You can make changes to the db with python3.6 manage.py makemigrations photos python3.6 manage.py migrate

## License

MIT

Copyright (c) {2019} **{KARINGE KINYUA}**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



