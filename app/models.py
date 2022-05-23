from django.db import models


# Create your models here.
class Carros(models.Model):
    objects = None
    seller_id = models.CharField(max_length=150)
    seller_zip_code_prefix = models.IntegerField()
    seller_city = models.CharField(max_length=150)
    seller_state = models.CharField(max_length=2)