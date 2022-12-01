from django.db import models



class Client(models.Model):
    
    
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    fatherland = models.CharField(max_length=20)
    number = models.CharField(max_length=21)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        
    def __str__(self):
        return f'Заказ клиента {self.name} '


    


