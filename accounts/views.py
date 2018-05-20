from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import *
 
 
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

class ProfileView(LoginRequiredMixin,ListView):
    def get_queryset(self):
        return None

