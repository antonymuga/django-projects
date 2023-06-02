from django.db import models

class Patron(models.Model):
    fname = models.CharField(max_length=255)
    mname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    mobile = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
