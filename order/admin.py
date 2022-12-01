from django.contrib import admin
from .models import PositionOrder
from .models import Order



class OrderAdmin(admin.ModelAdmin):
    list_display = ['client']


class POAdmin(admin.ModelAdmin):
    list_display = ['quantity', 'position_type']
    list_filter = ("position_type", )


admin.site.register(Order, OrderAdmin)
admin.site.register(PositionOrder, POAdmin)
