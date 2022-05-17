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
**Install all required packages (Django, Django-MultiSelectField, Pillow, Python-Decouple):**
```
pip install -r requirements.txt
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
**Example: Fetch and checkout the main branch:**
```
git checkout --track origin/main
```
<hr>

### Run Django Server:

In the root directory that has manage.py, place your SECRET_KEY and DEBUG values in an **.env** file. Make sure they are without quotation marks and whitespace. See [.env.example](family_plus/.env.example).

**To generate a SECRET KEY in the terminal use this command:**
```
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

**Make migrations and migrate the Django models to create the SQLite database:**
```
python manage.py makemigrations
```
```
python manage.py migrate
```

**Enable running Django server locally**
```
python manage.py runserver
```

On a web browser, enter localhost:8000 and you'll be at the Family+ welcome page.

[Back to Top](#family-web-app)