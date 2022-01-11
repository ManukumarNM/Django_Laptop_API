from django.contrib import admin

from .models import LaptopsModel
from django.contrib.admin.options import ModelAdmin

# Register your models here.
class LaptopAdmin(admin.ModelAdmin):
    list_display = ['brand', 'price']
admin.site.register(LaptopsModel, LaptopAdmin)