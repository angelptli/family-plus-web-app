# Family Plus Web App

Basic set up for running a Django server locally:

Notes: Django version 3.0+ is compatible with Python version 3.6+. 
See [requirements.txt](requirements.txt). The following guide is tailored for 
the [Git Bash](https://git-scm.com/downloads) terminal.

<hr>

## Python Virtual Environment:

**In an empty directory, create a Python virtual environment before preceding 
with the installation requirements (recommended):**
```
python -m venv virt
```
**Activate the Python virtual environment:**
```
. virt/Scripts/activate
```
<hr>

## Installation Requirements:

**Start with installing the latest version of Django:**
```
pip install django
```

**Then install Python Decouple to handle your keys:**
```
pip install python-decouple
```

**To support multi-selecting and storing, install django-multiselectfield:**
```
pip install django-multiselectfield
```

**Lastly install the Python Imaging Library for image handling:**
```
pip install pillow
```

<hr>

## Cloning & Fetching:

**Clone the repository:**
```
git clone https://github.com/angelptli/family-plus-web-app.git
```
**Move into the root directory which has the manage.py file:**
```
cd family-plus-web-app
```
**Fetch and checkout a specific branch simultaneously (recommended):**
```
git checkout --track origin/<branch-name>
```
**Example: Fetch and checkout the develop branch, which is maintained:**
```
git checkout --track origin/develop
```
<hr>

## Running the Django Server:

In the root directory that has manage.py, place your SECRET_KEY and DEBUG values 
(without the quotation marks and whitespace) in an **.env** file. 
See [.env.example](family_plus/.env.example).

**You can generate a SECRET KEY in the terminal using this command:**
```
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

**Make migrations and migrate the Django models to create the website's SQLite database:**
```
python manage.py makemigrations
```
```
python manage.py migrate
```

**Now you can locally run the Django server:**
```
python manage.py runserver
```

On a web browser, the website should run when you enter localhost:8000. You'll
be at the website's welcome page.
