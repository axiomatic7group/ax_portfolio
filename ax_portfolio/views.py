from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

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