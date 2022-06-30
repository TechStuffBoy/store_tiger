# store_tiger
This is a Django project. I am using SQlite Database for this and provided that file as well with this repo.

# Start Project

Create Virtual Env for the project <br>
```
$ python -m venv venv
$ source venv/bin/activate (Mac/Linux)
$ pip install -r requirements.txt
```

Run server
```
$ python manage.py runserver
```

To start freshly with a new database, just remove the provided dbsqlit3.
```
$ python manage.py migrate --> This will generate a new DB
```

Create superuser,
```
$ python manage.py createsuperuser   --> (currently, we have admin/12iso*help)
```

Please look at screenshot provided for reference.
