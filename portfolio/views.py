from django.shortcuts import render, redirect
from django.views import View
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from .models import *
from .forms import *

def check_authentication(check_request):
    if not check_request.user.is_authenticated:
        return redirect("/login")

class create_new_projects(View):
    def get(self, request):
        if check_authentication(request) != None:
            return check_authentication(request)

        new_project_form = add_new_projects(request.GET or None)

        context = {"new_project_form":new_project_form}
        return render(request, "portfolio/create_new_project.html", context)
    
    def post(self, request):
        if check_authentication(request) != None:
            return check_authentication(request)
        
        new_project_form = add_new_projects(request.POST or None)

        if new_project_form.is_valid():
            new_project = new_project_form.save(commit=False)
            new_project.date_created = timezone.now()
            new_project.save()

            new_project_form = add_new_projects()
            messages.success(request, 'project created')      

        context = {"new_project_form":new_project_form}
        return render(request, "portfolio/create_new_project.html", context)

class view_portfolio(View):
    def get(self, request):
        context = {}
        return render(request, "portfolio/view_portfolio.html", context)
    
    def post(self, request):
        context = {}
        return render(request, "portfolio/view_portfolio.html", context)