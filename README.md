# Travel Agency

SDA Albania Python from Scratch Course - Final Project

## Local development

Clone repository

```
git clone https://github.com/ArlindUkperaj/travel_agency.git
```

Enter cloned directory

```
cd travel_agency
```

Create virtual environment

```
python -m venv --prompt=trave-agency venv
. venv\Scripts\activate
python -m pip install -r requirements.txt
```

Run migrations to create database

```
python manage.py migrate
```

If you want to access admin, create a superuser

```
python manage.py createsuperuser
```

Run the local development server

```
python manage.py runserver
```