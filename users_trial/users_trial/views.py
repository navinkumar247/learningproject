from django.shortcuts import render
from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'

class LoggedInView(TemplateView):
    template_name = 'logged_in.html'

class LoggedOutView(TemplateView):
    template_name = 'thankyou.html'
