from django.apps import AppConfig


class MyappConfig(AppConfig):
    name = 'myApp'
    verbose_name = 'My first app' # Change the app name for the admin
    # for see the name update first go to settings and import MyappConfig