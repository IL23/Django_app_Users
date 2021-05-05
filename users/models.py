from django.db import models
from django.forms import ModelForm


class User(models.Model):

    username = models.CharField(max_length=125)
    email = models.CharField(max_length=125)


class UserForm(ModelForm):
    model = User
    fields = ['username', 'email']
