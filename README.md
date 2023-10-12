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


## How to add rest support 

`pip install djangorestframework`

see view api for example


path('project/projects', ProjectListCreateView.as_view(), name='project-list-create'),


 Json or APi doc available 

> http://127.0.0.1:8000/project/projects?format=api


## How to use authorization

in view use like 

```
     {% if request.user.is_authenticated %}
          {% if request.user.groups.all.0.name == 'operator' %} 

          <li class="nav-item">
            <a class="nav-link" href="/employee/show">Employee</a>
          </li>
 
          {% endif %} 
          {% endif %}  


```

and in method 

```
@login_required
@user_passes_test(lambda u: u.groups.filter(name='operator').exists())
def employee_lookup(request):

```

run  test cases using  `python3 manage.py test employee.tests.test`

## Loading sensitive configuration 

For loading info from .env file install `pip install python-decouple`

in setting.py

```
import os
from decouple import config


///For .env

DEBUG = config('DEBUG', cast=bool)
print("reading value from .env file---------------->"+str(DEBUG))

```

For OS

sudo nano ~/.bashrc add `export sample_variable=test` last line

verify:

```
source ~/.bashrc
cat ~/.bashrc
echo $sample_variable
```

`print("reading value from os env ---------------->"+str(os.environ.get('sample_varibale')))`


> In a production Django application, it's generally considered more secure to store sensitive information, such as database connection details and secret keys, in the host environment rather than in a .env file or hardcoding them in your project's code. Storing secrets in the host environment provides an extra layer of security and separation from your application code.





### To export dependencies

use this

`pip freeze > requirements.txt`



## Reference  

[Authentication-How to ](https://learndjango.com/tutorials/django-login-and-logout-tutorial)

[Authorization Tutorials](https://vegibit.com/understanding-djangos-authentication-and-authorization-system/)

[About Auth User Object](https://docs.djangoproject.com/en/4.2/ref/contrib/auth/)

[Getting Started](https://www.djangoproject.com/start/)

[How to guide](https://docs.djangoproject.com/en/4.2/howto/)

https://www.javatpoint.com/django-crud-application

