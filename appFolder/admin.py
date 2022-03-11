from django.contrib import admin
from .models import Hospital,Info

class InfoAdmin(admin.ModelAdmin):
    list_display = ("info_index","info_firstName","info_lastName","info_dateOfBirth","info_zipCode","info_vaccine","info_vaccineType","info_consentAck")
admin.site.register(Info, InfoAdmin) # For managing the app, register the model in admin page.

class HospitalAdmin(admin.ModelAdmin):
    list_display = ("hospital_id","hospital_name","hospital_address1","hospital_city","hospital_state","hospital_zipcode","hospital_x","hospital_y")

admin.site.register(Hospital,HospitalAdmin) # For managing the app, register the model in admin page.

