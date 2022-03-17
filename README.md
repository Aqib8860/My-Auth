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
- ![image](https://user-images.githubusercontent.com/67043041/158806969-2baaac15-45b0-4b12-9e09-ddd6feef32f0.png)

- http://127.0.0.1:8000/login - for Login
- ![image](https://user-images.githubusercontent.com/67043041/158807816-abdf3f6d-e46e-4c9d-ab36-75b86bf35324.png)

- http://127.0.0.1:8000/all_users  - for All Users List
- ![image](https://user-images.githubusercontent.com/67043041/158807860-9f4ffe60-f9d0-4cef-b7c7-3d39998b950a.png)

- http://127.0.0.1:8000/reset_password  - for Change Password
- ![image](https://user-images.githubusercontent.com/67043041/158808005-dff76111-ebdc-4f63-9380-9abfc3282799.png)


For sending the data in the api you will use Django Rest Framework provided Html form or send data in json format
