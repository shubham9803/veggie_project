from django.contrib import admin
from .models import Market

@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'state')
    search_fields = ('name', 'city', 'state')
