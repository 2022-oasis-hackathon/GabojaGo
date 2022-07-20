from django.db import models
from headquarters.models import Offender


# Create your models here.

class ScamData(models.Model):
    register_name = models.CharField(max_length=20)
    register_phone = models.CharField(max_length=30)
    site_name = models.CharField(max_length=40)
    transaction = models.CharField(max_length=20)
    object_name = models.CharField(max_length=100)
    site_link = models.CharField(max_length=1000)

    yong_id = models.CharField(max_length=20)
    yong_account = models.IntegerField()
    bank_name = models.CharField(max_length=20)
    account_name = models.ForeignKey(Offender, on_delete=models.CASCADE)
    trans_money = models.IntegerField()
    trans_date = models.DateTimeField()
    trans_phone = models.IntegerField()
    trans_sex = models.CharField(max_length=10)
    h_area1 = models.IntegerField()
    h_area2 = models.IntegerField()
