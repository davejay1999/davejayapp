# models.py
from django.db import models

class Bill(models.Model):
    patient_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    hospital_name = models.CharField(max_length=100)
    date_of_service = models.DateField()
    bill_amount = models.DecimalField(max_digits=8, decimal_places=2)
    bill_picture = models.ImageField(upload_to='bills/')