# django-auth

How to run this project
Install Python
Install & activate python virtual environment

Clone the project repo

go to the directory & run these commands:-
  - pip install -r requirements.txt
  - python manage.py makemigrations
  - python manage.py makemigrations users (this command is extra because of some migrations error in this project)
  - python manage.py migrate
  - python manage.py migrate users
  - python manage.py runserver

Go to the browser and hit th url
- http://127.0.0.1:8000/register - for registration
- http://127.0.0.1:8000/login - for Login
- http://127.0.0.1:8000/all_users  - for All Users List
- http://127.0.0.1:8000/change_password  - for Change Password

For sending the data in the api you will use Django Rest Framework provided Html form or send data in json format
