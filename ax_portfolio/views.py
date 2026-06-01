from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

import requests, markdown, json
import pandas as pd
from sqlalchemy import create_engine
from portfolio.forms import DetailedSignUpForm
from portfolio.models import campaign, campaign_funnel
from django.forms.models import model_to_dict
from django.conf import settings
from django.contrib import messages


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


class home_page(View):
    def get(self, request):
        funnel_id = 1       
        context = {}

        if campaign_funnel.objects.filter(id=funnel_id).exists():
            temp_campaign_funnel = campaign_funnel.objects.get(id=funnel_id)
            context['campaign_funnel'] = model_to_dict(temp_campaign_funnel)

            context["new_user_form"] = DetailedSignUpForm(request.GET or None)
            temp_input_form = json.loads(temp_campaign_funnel.funnel_input_form)
            for key in temp_input_form.keys():
                if not isinstance(temp_input_form[key], list):
                    temp_input_form[key] = [temp_input_form[key]]
            context["funnel_input_form"] = temp_input_form

            if temp_campaign_funnel.funnel_hero_img:
                context["funnel_hero_img"] = temp_campaign_funnel.funnel_hero_img
            else:
                with open(temp_campaign_funnel.funnel_hero_md, 'r', encoding='utf-8') as f:
                    text = f.read()
                context["funnel_hero_md"] = markdown.markdown(text)

            return render(request, "home.html", context)
        else:
            return redirect("/portfolio")
    
    def post(self, request):
        funnel_id = 1
        context = {}

        if campaign_funnel.objects.filter(id=funnel_id).exists():
            temp_campaign_funnel = campaign_funnel.objects.get(id=funnel_id)
            context['campaign_funnel'] = model_to_dict(temp_campaign_funnel)

            temp_funnel_name = str(temp_campaign_funnel.funnel_name).replace(" ", "_")

            temp_user_form = DetailedSignUpForm(request.POST)

            if temp_user_form.is_valid():
                new_user = temp_user_form.save(commit=False)
                new_user.save()
                temp_output_dict = {"user_id":str(new_user.id)}
                for key, value in json.loads(temp_campaign_funnel.funnel_input_form).items():
                    if key in request.POST.keys():
                        temp_output_dict[key] = request.POST[key]
                output_df = pd.DataFrame(temp_output_dict, index=[0])

                db_conf = settings.DATABASES['default']
                conn_string = f"postgresql://{db_conf['USER']}:{db_conf['PASSWORD']}@{db_conf['HOST']}:{db_conf['PORT']}/{db_conf['NAME']}"
                engine = create_engine(conn_string)
            
                try:
                    output_df.to_sql(temp_funnel_name, engine, if_exists="append", index=False)
                    messages.success(request, "Thank you for reaching out!.")
                except:
                    messages.warning(request, "Something went wrong, please try again.")
                


            context["new_user_form"] = DetailedSignUpForm(request.POST or None)
            temp_input_form = json.loads(temp_campaign_funnel.funnel_input_form)
            for key in temp_input_form.keys():
                if not isinstance(temp_input_form[key], list):
                    temp_input_form[key] = [temp_input_form[key]]
            context["funnel_input_form"] = temp_input_form
            
            if temp_campaign_funnel.funnel_hero_img:
                context["funnel_hero_img"] = temp_campaign_funnel.funnel_hero_img
            else:
                with open(temp_campaign_funnel.funnel_hero_md, 'r', encoding='utf-8') as f:
                    text = f.read()
                context["funnel_hero_md"] = markdown.markdown(text)

        return render(request, "home.html", context)