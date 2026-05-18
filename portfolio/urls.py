from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("create_new_project/", views.create_new_projects.as_view(), name="create_new_project_view")

]
