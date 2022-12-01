from django.contrib import admin
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'fatherland', 'number']
    search_fields = ("number", )
    list_filter = ("surname", )

admin.site.register(Client, ClientAdmin)