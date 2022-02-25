from django.contrib import admin
from .models import Hospital,Info

class InfoAdmin(admin.ModelAdmin):
    list_display = ("info_index","info_firstName","info_lastName","info_dateOfBirth","info_zipCode","info_vaccine","info_vaccineType","info_consentAck")
admin.site.register(Info, InfoAdmin) # For managing the app, register the model in admin page.
admin.site.register(Hospital) # For managing the app, register the model in admin page.

