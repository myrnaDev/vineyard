from django.db import models

class Wine(models.Model):
    id = models.IntegerField(primary_key=True)
    wine_name = models.CharField(max_length=255)
    wine_variety = models.CharField(max_length=255)
    wine_type = models.CharField(max_length=255)
    wine_region = models.CharField(max_length=100)
    wine_stock = models.IntegerField(max_length=100)
