from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import *

class DescView(ListView):
    def get_queryset(self):                                                       
        return None
