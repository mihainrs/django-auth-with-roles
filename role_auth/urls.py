from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', auth_views.LoginView.as_view(template_name= 'role_auth/login.html'), name='login'),
    path('logout', views.custom_logout, name='logout'),
    path('signup',views.signup, name='signup'),
]