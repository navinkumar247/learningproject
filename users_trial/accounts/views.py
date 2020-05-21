from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from .models import User
from .forms import UserCreateForm
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.
UserModel = get_user_model()

class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/user_signup.html'

# class UserList(ListView):
#     model = User
#
class UserDetail(DetailView):
    
    model = UserModel

# class UserUpdate(UpdateView,LoginRequiredMixin):
#     model = UserModel
#     fields = ('username','email','password1','password2')
#
# class UserDelete(DeleteView,LoginRequiredMixin):
#     model = UserModel
