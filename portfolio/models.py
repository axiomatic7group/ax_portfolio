from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[0-9a-zA-Z ]*$', 'Only alphanumeric characters are allowed.')

project_type_list = [
    ('open_source', 'Open Source'),
    ('research', 'Research'),
    ('client', 'Client'),
    ('propietary', 'Proprietary'),
    ('other', 'Other'),
]

class portfolio_projects(models.Model):
    date_created = models.DateField('date created', default=timezone.now)
    project_name = models.CharField(max_length=254)
    project_description = models.TextField()
    project_casestudy = models.TextField()
    project_repo_link = models.CharField(max_length=254)
    project_hero_image = models.CharField(max_length=254, blank=True, null=True)
    project_type = models.CharField(max_length=75, choices=project_type_list)

class campaign(models.Model):
    date_created = models.DateField('date created', default=timezone.now)
    campaign_name = models.CharField(max_length=254, validators=[alphanumeric])
    campaign_description = models.TextField()

class campaign_funnel(models.Model):
    funnel_name = models.CharField(max_length=254, validators=[alphanumeric], unique=True)
    funnel_campaign = models.ForeignKey(campaign, on_delete=models.CASCADE)
    funnel_input_form = models.TextField(default='{"message":"placeholder"}')
    funnel_hero_img = models.CharField(max_length=350, blank=True, null=True)
    funnel_hero_md = models.CharField(max_length=350, blank=True, null=True)