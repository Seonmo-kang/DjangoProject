from django.db import models

# Create your models here.
class Info(models.Model):
    info_index = models.BigAutoField("indexNum",primary_key=True) # Auto incredent number
    info_zipCode = models.IntegerField("zipcode") # Zipcode
    info_dateOfBirth = models.DateField("date of birth",help_text="YYYY/MM/DD") # Date of Birth
    FirstDose = 'fd'
    BoosterDose = 'bd'
    AdditionalDose = 'ad'
    VACCINE_IN_CHOICES = [
        (FirstDose,'First Dose'),
        (BoosterDose, 'Booster Dose'),
        (AdditionalDose, 'Additional Dose')
    ]
    info_vaccine = models.CharField("vaccine",max_length=20,choices=VACCINE_IN_CHOICES) # 1 : First Dose , 2 : Booster Dose, 3 : Additional Dose
    info_vaccineType = models.CharField("vaccine type",max_length=20) # VaccineType 1: Pfizer 2: Janssen
    info_consentAck = models.BooleanField("consent Ack") # consent Acknowledgement

class Hospital(models.Model):
    Hospital_name = models.CharField('Hospital name',max_length=20, primary_key=True)
    Hospital_address1 = models.CharField('Hospital address1',max_length=20)
    Hospital_address2 = models.CharField('Hospital address2',max_length=200,blank=True) #Address2 is optional
    Hospital_city = models.CharField('Hospital city',max_length=20)
    Hospital_state = models.CharField('Hospital state',max_length=10)
    Hospital_zipcode = models.IntegerField('Hospital zipcode', default=00000)   #Hospital zipcode
    #Hospital_vaccineType = models.CharField
    # Hospital_vaccineType = models. # vaccine could be multi...
