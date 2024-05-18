from django.db import models

class UserInput(models.Model):
    age = models.IntegerField()
    bmi = models.FloatField()
    blood_pressure = models.FloatField()
