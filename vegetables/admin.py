from django.contrib import admin
from .models import Vegetable

@admin.register(Vegetable)
class VegetableAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'marathi_name')
    search_fields = ('name', 'marathi_name')
