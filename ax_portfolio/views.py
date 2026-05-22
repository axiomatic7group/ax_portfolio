from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

import markdown, requests
from portfolio.forms import DetailedSignUpForm

class authenticate_users(View):
    def get(self, request):
        user_auth_form = AuthenticationForm(request.GET or None)

        context = {'user_auth_form':user_auth_form}
        return render(request, './login.html', context)
    
    def post(self, request):
        user_auth_form = AuthenticationForm(data=request.POST)

        if user_auth_form.is_valid():
            username = user_auth_form.cleaned_data.get('username')
            password = user_auth_form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                
                return redirect('/portfolio')

        context = {'user_auth_form':user_auth_form}
        return render(request, './login.html', context)

class about_us(View):
    def about_us(request):
        context = {}

        with open('about_us.md', 'r', encoding='utf-8') as f:
            text = f.read()

        context['content'] = markdown.markdown(text)

        return render(request, './about_us.html', context)
    
    def privacy(request):
        context = {}

        with open('privacy_policy.md', 'r', encoding='utf-8') as f:
            text = f.read()

        context['content'] = markdown.markdown(text)

        return render(request, './privacy.html', context)
    
    def terms(request):
        context = {}

        with open('terms_of_service.md', 'r', encoding='utf-8') as f:
            text = f.read()

        context['content'] = markdown.markdown(text)

        return render(request, './terms.html', context)

class contact_us(View):
    def get(self, request):
        context = {}

        DetailedSignUpForm_form = DetailedSignUpForm(request.GET or None)

        context['DetailedSignUpForm_form'] = DetailedSignUpForm_form

        return render(request, './contact_us.html', context)
    
    def post(self, request):
        context = {}

        if request.method == 'POST':
            DetailedSignUpForm_form = DetailedSignUpForm(request.POST)
            if DetailedSignUpForm_form.is_valid():
                DetailedSignUpForm_form.save()
                
                return redirect('/login')
        else:
            DetailedSignUpForm_form = DetailedSignUpForm()

        context['DetailedSignUpForm_form'] = DetailedSignUpForm_form
        return render(request, './contact_us.html', context)


