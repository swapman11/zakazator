from django.db import models


class Product(models.Model):
   
    name = models.CharField(max_length=90)
    description = models.TextField(null=True)
    price = models.FloatField()


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'