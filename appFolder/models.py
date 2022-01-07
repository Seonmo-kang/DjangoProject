from django.db import models

# Create your models here.
class Info(models.Model):
    info_index = models.BigAutoField("indexNum",primary_key=True) # Auto incredent number
    info_dateOfBirth = models.DateField("date of birth",help_text="DD/MM/YY") # Date of Birth
    info_zipCode = models.IntegerField("zipcode",max_length=5) # Zipcode
    info_vaccine = models.CharField("vaccine",max_length=20) # 1 : First Dose , 2 : Booster Dose, 3 : Additional Dose
    info_vaccineType = models.CharField("vaccine type",max_length=20) # VaccineType 1: Pfizer 2: Janssen
    info_consentAck = models.BooleanField("consent Ack") # consent Acknowledgement

