# poc-django



## After change

`python3 manage.py makemigrations`

`python3 manage.py migrate`

`python3 manage.py runserver`

To reset db `python3 manage.py reset_db`

## Create new super user in admin

`python3 manage.py createsuperuser`

## How to Install shell plus

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

### How to use Shell Plus


`python3 manage.py shell_plus --ipython`

`data=Employee.objects.all()`

`for employee in data: print(employee.ename)`

### Filter

emplist = Employee.objects.filter(eid='12')
for employee in emplist:    print(employee.ename)

### Get
in model
eid = models.CharField(max_length=20, unique=True)

command

employees_with_eid_12 = Employee.objects.get(eid='12')
print(employees_with_eid_12.ename)


## Troubleshoot

### Table not added 

> make sure model are added in `admin.py`

### Static file problem

in settings use 

```
import os

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
VENV_PATH = os.path.dirname(BASE_DIR)
STATIC_ROOT = os.path.join(VENV_PATH, 'static_root')

```
https://docs.djangoproject.com/en/4.2/howto/static-files/


## Reference  

[Authentication-How to ](https://learndjango.com/tutorials/django-login-and-logout-tutorial)

[Getting Started](https://www.djangoproject.com/start/)

[How to guide](https://docs.djangoproject.com/en/4.2/howto/)

https://www.javatpoint.com/django-crud-application

