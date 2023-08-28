# poc-django

django poc 

https://www.javatpoint.com/django-crud-application


python3 manage.py runserver

## Create new super user in admin

`python3 manage.py createsuperuser`



## Troubleshoot

in settings 

```
import os

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
VENV_PATH = os.path.dirname(BASE_DIR)
STATIC_ROOT = os.path.join(VENV_PATH, 'static_root')

```


