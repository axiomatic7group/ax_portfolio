from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("campaign/<slug:funnel_id>", views.view_campaign_funnel.as_view(), name="view_campaign_funnel_view"),
    path("campaign_all/<slug:funnel_id>", views.view_campaign_funnel.see_all_info, name="all_campaign_funnel_view"),
    path("create_campaign_funnel/", views.create_campaign_funnel.as_view(), name="create_campaign_funnel_view"),
    path("create_new_project/", views.create_new_projects.as_view(), name="create_new_project_view"),
    path("view_project/<slug:project_id>", views.view_project.as_view(), name="view_project_view"),
    path("", views.view_portfolio.as_view(), name="view_portfolio_view"),

]
