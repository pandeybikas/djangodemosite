from django.urls import path
from . import views
from django.contrib.auth import views as authentication_view

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', authentication_view.LoginView.as_view(template_name= 'users/login.html ' ), name='login'),
    path('logout', authentication_view.LogoutView.as_view(template_name= 'users/logout.html ' ), name='logout'),
    path('account', views.ProfilePage, name='account'),
    path('create_profile', views.create_profile, name='create_profile')
]
