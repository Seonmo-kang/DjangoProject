from django.contrib import admin
from .models import Hospital,Info
# Register your models here.
admin.site.register(Info) # For managing the app, register the model in admin page.
admin.site.register(Hospital) # For managing the app, register the model in admin page.