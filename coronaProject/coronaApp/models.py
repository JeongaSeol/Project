from django.db import models

# Create your models here.
class coronaDate(models.Model):
    date = models.CharField(max_length=50)
    confirmed = models.IntegerField(default=0)

class coronaDistrict(models.Model):
    rank = models.IntegerField(default=0)
    district = models.CharField(max_length=10)
    confirmed = models.IntegerField(default=0)

class vaccineRate(models.Model):
    district = models.CharField(max_length=10)
    rate = models.DecimalField(max_digits = 5, decimal_places=2)

class vaccinepercorona(models.Model):
    district = models.CharField(max_length=10)
    rate = models.DecimalField(max_digits = 5, decimal_places=2)

class Board(models.Model):
    content = models.CharField(max_length=255)