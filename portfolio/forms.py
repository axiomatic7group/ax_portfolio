from django.forms import ModelForm
from django import forms

from .models import *

class add_new_projects(ModelForm):

    class Meta:
        model = portfolio_projects
        exclude = ['date_created', 'project_hero_image']
        fields = "__all__"
