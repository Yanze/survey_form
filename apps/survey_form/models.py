from django.db import models
from django import forms


# Create your models here.

class Form(forms.Form):
    name = forms.CharField(error_messages={'required': 'Please enter your name'})
    location = forms.CharField()
    language = forms.CharField()
    comment = forms.CharField(error_messages={'required': 'Please enter your comment'})
