from django.forms import ModelForm
from .. import models
class InfoForm(ModelForm):
    class Meta:
        model = models.Info
        fields = '__all__'
        # self.info_firstName = customer_data["firstName"]
        # self.info_lastName = customer_data["lastName"]
        # self.info_dateOfBirth = customer_data["birthOfDate"]
        # self.info_state = customer_data["state"]
        # self.zipCode = customer_data["zipcode"]
        # self.vaccine = customer_data["vaccine"]
        # self.vaccineType = customer_data["vaccineType"]
        # self.consentAck = customer_data["consentAck"]
        # self.info_hospital_id = customer_data["hospital"]
