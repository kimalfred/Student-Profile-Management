# Student Profile Managemnet System Using Django

![image](https://github.com/kimalfred/Student-Profile-Management/assets/119164038/43ca64c7-6166-4060-ac58-74a0dc9d7eee)

## Templates

-Free themes for Bootstrap (Website from [here](https://bootswatch.com/))

-Free Icons (Website from [here](https://fontawesome.com/))


## Installation

1. Set up a virtual environment
   First, create and activate a virtual environment:
```bash
python -m venv venv
venv\scripts\activate
```
2. Install Django
   Install Django using pip:
```bash
pip install django
```
3. Start a new Django project
Create a new Django project named django_project or any name:
```bash
django-admin startproject django_project.
```
4. Run the server
   Navigate to the project directory and run the server:
```bash
python manage.py runserver
```
5. Create a new app
   Create a new app called students:
```bash
python manage.py startapp students
```
6. Make migrations and migrate
   Apply initial migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```
7. Create an Admin User to Access the Django Admin Interface
From the root directory, run:
```
python manage.py createsuperuser
```
