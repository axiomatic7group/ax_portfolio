from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms
from django.utils.safestring import  mark_safe

from .models import *


class DetailedSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    agree_to_terms = forms.BooleanField(
        required=True,
        label=mark_safe(
            'I have read and agree to the <a href="/terms/" target="_blank" rel="noopener">Terms of Use</a> '
            'and acknowledge the data processing practices described in the '
            '<a href="/privacy/" target="_blank" rel="noopener">Privacy Policy</a>.'
        ),
        error_messages={
            'required': 'You must accept the Terms of Use and acknowledge the Privacy Policy to proceed.'
        }
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')
    
    def clean_email(self):
        """Checks if the email is already registered in the database."""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with that email already exists.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        user.is_staff = False  
        
        if commit:
            user.save()
        return user

class add_new_projects(ModelForm):

    class Meta:
        model = portfolio_projects
        exclude = ['date_created', 'project_hero_image']
        fields = "__all__"


class add_new_campaign_funnel(ModelForm):

    class Meta:
        model = campaign_funnel
        fields = "__all__"