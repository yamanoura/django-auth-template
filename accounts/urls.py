from django.urls import path
 
from . import views
 
app_name = 'accounts'
 
urlpatterns = [
    path('signup/', views.SignUpView.as_view(template_name='%s/signup.html' % app_name), name='signup'),
    path('profile/', views.ProfileView.as_view(template_name='%s/profile.html' % app_name), name='profile'),    
]
