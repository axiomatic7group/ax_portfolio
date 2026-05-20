from django.shortcuts import render, redirect
from django.views import View
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.forms.models import model_to_dict

import requests, markdown

from .models import *
from .forms import *

def check_authentication(check_request):
    if not check_request.user.is_authenticated:
        return redirect("/login")
    elif not check_request.user.is_staff:
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

class view_project(View):
    def get(self, request, project_id):
        
        context = {}

        if portfolio_projects.objects.filter(id=project_id).exists():
            project_to_see = portfolio_projects.objects.get(id=project_id)
       
            get_github_info = requests.get(f"https://api.github.com/repos/{project_to_see.project_repo_link}")
            get_github_readme = requests.get(f"https://api.github.com/repos/{project_to_see.project_repo_link}/readme", headers={"Accept": "application/vnd.github.raw+json"})
            if get_github_readme.status_code == 200:
                github_readme = get_github_readme.text
                context['github_readme'] = markdown.markdown(github_readme)
            
            if get_github_info.status_code == 200:
                github_info = get_github_info.json()
                context['github_info'] = github_info

            context['project_to_see'] = model_to_dict(project_to_see)

            return render(request, "portfolio/view_project.html", context)
        else:
            redirect('/portfolio')
    
    def post(self, request, project_id):
        
        context = {}

        if portfolio_projects.objects.filter(id=project_id).exists():
            project_to_see = portfolio_projects.objects.get(id=project_id)
       
            get_github_info = requests.get(f"https://api.github.com/repos/{project_to_see.project_repo_link}")
            get_github_readme = requests.get(f"https://api.github.com/repos/{project_to_see.project_repo_link}/readme", headers={"Accept": "application/vnd.github.raw+json"})
            if get_github_readme.status_code == 200:
                github_readme = get_github_readme.text
                context['github_readme'] = markdown.markdown(github_readme)
            
            if get_github_info.status_code == 200:
                github_info = get_github_info.json()
                context['github_info'] = github_info

            context['project_to_see'] = model_to_dict(project_to_see)

            return render(request, "portfolio/view_project.html", context)
        else:
            redirect('/portfolio')

class view_portfolio(View):
    def get(self, request):
        context = {}

        get_all_projects = portfolio_projects.objects.all()

        context['all_projects'] = get_all_projects.values()

        return render(request, "portfolio/view_portfolio.html", context)
