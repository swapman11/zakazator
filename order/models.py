from django.db import models
from clients.models import Client
from product.models import Product
from simple_history.models import HistoricalRecords

class OrderStatus(models.Model):
    name = models.CharField(verbose_name='Название', max_length=60)
    history = HistoricalRecords()
    class Meta:
        verbose_name = "Статус заказа"
        verbose_name_plural = "Статусы заказов"


class Order(models.Model):
    create_date = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
        blank=True,
        null=True
    )
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.ForeignKey(OrderStatus,
                               on_delete=models.PROTECT,
                               verbose_name='Статус зазака',
                               null=True, blank=True)

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return f'Заказ {self.id} {self.client.name}'


class PositionOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.FloatField(verbose_name='Кол-во ')
    product = models.ForeignKey(Product,
                                on_delete=models.PROTECT,
                                null=True,
                                blank=True,
                                verbose_name='Продукт')

    class Meta:
        verbose_name = 'позиция заказа'
        verbose_name_plural = 'Позиции заказов'
