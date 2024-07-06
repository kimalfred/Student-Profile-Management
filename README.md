### Installation

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
<<<<<<< HEAD
   Create a new Django project named django_project:

=======
Create a new Django project named django_project or any name:
>>>>>>> 1519c3404ecb13c5cae2134ac132d5e4c237dc1e
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
