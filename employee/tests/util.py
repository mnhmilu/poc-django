# authapp/utils.py

from django.contrib.auth.models import User

def is_operator(user):
    print(user.get_username())
    print(user.groups.filter(name='operator').exists())
    return user.groups.filter(name='operator').exists()
