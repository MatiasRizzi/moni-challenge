from django.db import models

class Loan(models.Model):
    number_dni = models.IntegerField(null=False)
    name = models.TextField(null=True, max_length=200)
    surname = models.TextField(null=True, max_length=200)
    gender = models.TextField(null=True, max_length=200) #TODO choice
    email = models.EmailField(null=True)
    requested_amount = models.IntegerField(null=True)

