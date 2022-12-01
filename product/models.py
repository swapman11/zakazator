from django.db import models


class Product(models.Model):
   
    name = models.CharField(max_length=90)
    description = models.CharField(null=True, max_length=250)
    price = models.FloatField()

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'