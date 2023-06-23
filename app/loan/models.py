from django.db import models

class Loan(models.Model):
    number_dni = models.IntegerField(null=False, max_length=10)
    name = models.TextField(null=True, max_length=200)
    surname = models.TextField(null=True, max_length=200)
    gender = models.TextChoices(null=True, max_length=200) #TODO choice
    email = models.EmailField(null=True)
    requested_amount = models.IntegerField(null=True)

