from django.forms import ModelForm
from django import forms

from .models import *

class add_new_projects(ModelForm):

    class Meta:
        model = portfolio_projects
        exclude = ['date_created']
        fields = "__all__"
