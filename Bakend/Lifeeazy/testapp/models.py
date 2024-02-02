from django.db import models

LIST_PARTNER = (
    ('Clinic', 'Clinic'),
    ('Hospital', 'Hospital'),
    ('Diagnostic', 'Diagnostic'),
    ('pharmacy', 'pharmacy'),)
# Create your models here.
class Topping(models.Model):
    name = models.CharField(max_length=100,choices=LIST_PARTNER,)
    vaccine = models.CharField(max_length=100)
    objects = models.Manager
    class Meta:
        db_table='test_table'


class Pizza(models.Model):
    name = models.CharField(max_length=100)
    vaccine = models.ManyToManyField(Topping,name= "Hospital")
    objects = models.Manager

    class Meta:
        db_table = 'second_table'