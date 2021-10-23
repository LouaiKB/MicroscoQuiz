from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from users.views import login_page, register_page

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register')
]
