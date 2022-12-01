from django.db import models
from clients.models import Client



class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'


    def __str__(self):
        return f'Заказ {self.id} {self.client.name}'



class PositionOrder(models.Model):
    n = 1
    p = 2
    v = 3
    ch = 4
    vz = 5
    POSITION_TYPE = (
        (n, 'На сборке у продавца'),
        (p, 'На проверке у таможни'),
        (v, 'В пункте выдачи'),
        (ch, 'ЧС'),
        (vz, 'Возврат'),     
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.FloatField()
    position_type = models.PositiveSmallIntegerField(null=True, choices=POSITION_TYPE)
    class Meta:
        verbose_name = 'позиция заказа'
        verbose_name_plural = 'Позиции заказов'