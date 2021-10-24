from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView

class LoginFormView(SuccessMessageMixin, LoginView):
    template_name = "users\\login.html"
    success_message = "You were successfully logged in."

class LogoutFormView(SuccessMessageMixin, LogoutView):
    template_name = "users\\logout.html"
    # success_message = "You were successfully logged out."