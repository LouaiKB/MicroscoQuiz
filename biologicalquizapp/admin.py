from django.contrib import admin
from .models import *
from users.models import *

# Register your models here.
admin.site.register(Image)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Profile)