"""
URL configuration for ax_portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('portfolio/', include("portfolio.urls")),
    path('admin/', admin.site.urls),
    path('login/', views.authenticate_users.as_view(), name='login_html'),
    path('contact/', views.contact_us.as_view(), name='contact_us_html'),
    path('about/', views.about_us.about_us, name='about_us_html'),
    path('privacy/', views.about_us.privacy, name='privacy_html'),
    path('terms/', views.about_us.terms, name='terms_html'),
    path('llms/', views.about_us.llms, name='llms_html'),
    path('', views.home_page.as_view(), name='home_page_html'),

]
