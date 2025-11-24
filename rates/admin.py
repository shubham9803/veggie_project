from django.contrib import admin
from .models import Rate


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'vegetable',
        'market',
        'quantity',
        'price',
        'added_by',
        'verified_by',
        'is_verified',
        'created_at',
    )

    list_filter = ('is_verified', 'market', 'vegetable')

    search_fields = (
        'vegetable__name',
        'vegetable__marathi_name',
        'market__name',
        'added_by__username',
        'verified_by__username'
    )

    readonly_fields = ('created_at',)
