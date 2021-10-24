"""quizapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from users.views import register_page, login_page
from users.log_form_view import LoginFormView, LogoutFormView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/', LoginView.as_view(template_name="users\\login.html"), name='login'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name="users\\logout.html"), name='logout'),
    path('register/', register_page, name='register'),
    path('', include("biologicalquizapp.urls")),
]
