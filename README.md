# poc-django



## After change

python3 manage.py makemigrations 

python3 manage.py migrate 


python3 manage.py runserver

## Create new super user in admin

`python3 manage.py createsuperuser`

## How to use shell plus

```
pip install ipython==7.3.0
pip install ipython-genutils==0.2.0
pip install django-extensions==2.1.7
pip install jedi==0.17

```

in settins:

```
INSTALLED_APPS = [
    ...
    'django_extensions',
]

```

python3 manage.py shell_plus --ipython

data=Employee.objects.all()

for employee in data: print(employee.ename)



## Troubleshoot

in settings 

```
import os

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
VENV_PATH = os.path.dirname(BASE_DIR)
STATIC_ROOT = os.path.join(VENV_PATH, 'static_root')

```


## Reference  

https://www.javatpoint.com/django-crud-application

