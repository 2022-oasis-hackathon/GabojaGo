from django.db import models

# Create your models here.

class Offender(models.Model):
    name = models.CharField(max_length=20)
    arrest_status = models.BooleanField(default=False)

