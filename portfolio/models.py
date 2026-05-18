from django.db import models
from django.utils import timezone

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