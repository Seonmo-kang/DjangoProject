from django.test import TestCase
from .models import Info

# After have database done.
# class InfoFormModelTest(TestCase):
#     def setUpClass(self):
#         Info.objects.create(
#             info_index=1,
#             info_dateOfBirth= '1996/01/02',
#             info_zipCode= 12345,
#             info_vaccine= 'fd',
#             info_vaccineType='Pfizer',
#             info_consentAck='True'
#         )
#     def test_infoForm