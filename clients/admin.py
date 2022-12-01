from django.contrib import admin
from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'fatherland', 'number']
    search_fields = ("number", 'name', 'surname')
    list_filter = ("surname",)
