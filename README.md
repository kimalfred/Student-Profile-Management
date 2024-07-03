### Installation
1. Set up a virtual environment
First, create and activate a virtual environment:
```
python -m venv venv
venv\scripts\activate
```
2. Install Django
Install Django using pip:
```
pip install django
```
3. Start a new Django project
Create a new Django project named django_project:
```
django-admin startproject django_project .
```
4. Run the server
Navigate to the project directory and run the server:
```
python manage.py runserver
```
5. Create a new app
Create a new app called students:
```
python manage.py startapp students
```
6. Make migrations and migrate
Apply initial migrations:
```
python manage.py makemigrations
python manage.py migrate
```
