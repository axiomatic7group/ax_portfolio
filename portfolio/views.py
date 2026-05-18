from django.shortcuts import render
from django.views import View
from django.utils import timezone
from django.contrib import messages


from .models import *
from .forms import *


class create_new_projects(View):
    def get(self, request):
        new_project_form = add_new_projects(request.GET or None)

        context = {"new_project_form":new_project_form}
        return render(request, "portfolio/create_new_project.html", context)
    
    def post(self, request):
        new_project_form = add_new_projects(request.POST or None)

        if new_project_form.is_valid():
            new_project = new_project_form.save(commit=False)
            new_project.date_created = timezone.now()
            new_project.save()

            new_project_form = add_new_projects()
            messages.success(request, 'project created')      

        context = {"new_project_form":new_project_form}
        return render(request, "portfolio/create_new_project.html", context)

