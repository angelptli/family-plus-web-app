# Family Plus Web App

Basic set up for running a Django server locally:

Django version 3.0+ is compatible with Python version 3.6+. See [requirements.txt](requirements.txt).

**Start with installing the latest version of Django:**
```
$ pip install django
```

**You'll need to install Python Decouple to handle your keys:**
```
$ pip install python-decouple
```

**Lastly install the Python Imaging Library for image handling:**
```
$ pip install pillow
```

Place your SECRET_KEY and DEBUG values (without the quotation marks and whitespace) in the **.env** file. The **.env** should be placed in the same directory as manage.py. See [.env.example](family_plus/.env.example).

**Run the Django server in the directory that has manage.py:**
```
$ python manage.py runserver
```

On a web browser, the website should run when you enter localhost:8000.
