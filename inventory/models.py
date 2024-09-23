from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField( max_length=255, blank=False )
    quantity = models.IntegerField( default=0 )
    sku = models.CharField( max_length=255, unique=True )
    brand = models.CharField(max_length=255)
    created_date = models.DateTimeField( auto_now_add=True )
    description = models.CharField( max_length=255, blank=True )


    def __str__(self) -> str:
        return self.name

class Dimension(models.Model):
    height = models.FloatField(default=0)
    weight = models.FloatField(default=0)

class Characteristic(models.Model):
    product = models.ForeignKey( Product, on_delete=models.CASCADE )
    dimension = models.ForeignKey(Dimension, on_delete=models.CASCADE)
    color = models.CharField(max_length=255, blank=True)
    material_type = models.CharField(max_length=255, blank=True )


class Price(models.Model):
    product = models.ForeignKey( Product, on_delete=models.CASCADE )
    amount = models.IntegerField( default=0 )

class discount(models.Model):
    product = models.ForeignKey( Product, on_delete=models.CASCADE )
    porcentage = models.FloatField(default=0 )
    amount = models.IntegerField(default=0)

class Category(models.Model):
    name = models.CharField(max_length=255)

class CategoryProduct(models.Model):
    product_id = models.ForeignKey( Product, on_delete=models.CASCADE )
    category_id = models.ForeignKey( Category, on_delete=models.CASCADE )

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    phone = models.IntegerField(default=0)
    contact_email = models.IntegerField( null=False )