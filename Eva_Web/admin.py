from django.contrib import admin
from .models import Client, Category,Product
# Register your models here.
admin.site.register(Client)
admin.site.register(Category)
admin.site.register(Product)