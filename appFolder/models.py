from django.db import models
from django.core.validators import RegexValidator

# Address validator
zipcodeValidator = RegexValidator(r"^([0-9]{5}(?:-[0-9]{4})?$)",'Must be 00000 or 00000-0000','This is code')

# Info DB : user information input
class Info(models.Model):
    info_index = models.BigAutoField("indexNum",primary_key=True) # Auto incredent number
    info_dateOfBirth = models.DateField("date of birth",help_text="YYYY/MM/DD") # Date of Birth
    info_zipCode = models.CharField("zipcode",max_length=11,default="10001",
                                    validators=[zipcodeValidator])
        # RegexValidator(regex=r"^([0-9]{5}(?:-[0-9]{4})?$)",message='Must be 00000 or 00000-0000',code='This is code')
        # # I would like to reuse RegexValidator(regex=r'^([0-9]{5}(?:-[0-9]{4})?$)')
        # So i make RegexValidator object with zipcodeValidator
        # Zipcode validator ( 12345 or 12345-1234 )
    #Vaccine
    FirstDose = 'fd'
    BoosterDose = 'bd'
    AdditionalDose = 'ad'
    VACCINE_IN_CHOICES = [
        (FirstDose,'First Dose'),
        (BoosterDose, 'Booster Dose'),
        (AdditionalDose, 'Additional Dose')
    ]
    info_vaccine = models.CharField("vaccine",max_length=2,choices=VACCINE_IN_CHOICES) # 1 : First Dose , 2 : Booster Dose, 3 : Additional Dose
    #VaccineType
    pfizer = 'pf'
    janssen = 'js'
    VACCINETYPE_IN_CHOICES = [
        (pfizer, 'pfizer'),
        (janssen,'janssen')
    ]
    info_vaccineType = models.CharField("vaccine type",max_length=2,choices=VACCINETYPE_IN_CHOICES) # VaccineType 1: Pfizer 2: Janssen
    info_consentAck = models.BooleanField("consent Ack") # consent Acknowledgement

# Hospital DB
class Hospital(models.Model):
    hospital_name = models.CharField('Hospital name',max_length=30, primary_key=True)
    hospital_address1 = models.CharField('Hospital address1',max_length=20)
    hospital_address2 = models.CharField('Hospital address2',max_length=200,blank=True) #Address2 is optional
    hospital_city = models.CharField('Hospital city',max_length=20)
    hospital_state = models.CharField('Hospital state',max_length=10)
    hospital_zipcode = models.CharField('Hospital zipcode', max_length=11, default='10001',validators=[zipcodeValidator])   #Hospital zipcode

    pfizer = 'pf'
    janssen = 'js'
    all = 'all'
    VACCINETYPE_IN_CHOICE = [
        (pfizer, 'pfizer'),
        (janssen,'janssen'),
        (all,'all')]
    hospital_vaccineType = models.CharField('Hospital vaccineType', max_length=4, choices=VACCINETYPE_IN_CHOICE)

    def __str__(self):
        return self.Hospital_name[:100]