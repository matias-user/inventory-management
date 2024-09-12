from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField( max_length=255, blank=False )
    quantity = models.IntegerField( default=0 )
    sku = models.CharField( max_length=255 )


class Price(models.Model):
    product = models.ForeignKey( Product, on_delete=models.CASCADE )
    amount = models.IntegerField( default=0 )


class discount(models.Model):
    product = models.ForeignKey( Product, on_delete=models.CASCADE )
    porcentage = models.FloatField(default=0 )
    amount = models.IntegerField(default=0)