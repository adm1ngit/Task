from django.db import models

class Warehouse(models.Model):
    name = models.CharField(max_length=100)

class Material(models.Model):
    name = models.CharField(max_length=100)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    remaining_quantity = models.IntegerField()
    price = models.FloatField()

class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    materials = models.ManyToManyField(Material, through='ProductMaterial')

class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.IntegerField()
