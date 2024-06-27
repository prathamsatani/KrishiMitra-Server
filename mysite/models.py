from django.db import models

class Signup(models.Model):
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)