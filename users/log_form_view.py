from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView

class LoginFormView(SuccessMessageMixin, LoginView):
    template_name = "users\\login.html"
    success_message = "You were successfully logged in."
