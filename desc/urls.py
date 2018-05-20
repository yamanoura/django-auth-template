from django.urls import path
 
from . import views
 
# set the application namespace
# https://docs.djangoproject.com/en/2.0/intro/tutorial03/
app_name = 'desc'
 
urlpatterns = [
    path('', views.DescView.as_view(template_name='%s/desc.html' % app_name), name='desc'),
]
