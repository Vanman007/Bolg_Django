from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import revers_lazy
from django.views import generic

 class SignUpView(generic.CreateView):
     form_class = UserCreationForm
     sucess_url = reverse_lazy('login')
     template_name = 'signup.html'
