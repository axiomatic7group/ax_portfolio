from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("create_new_project/", views.create_new_projects.as_view(), name="create_new_project_view"),
    path("view_project/<slug:project_id>", views.view_project.as_view(), name="view_project_view"),
    path("", views.view_portfolio.as_view(), name="view_portfolio_view"),

]
