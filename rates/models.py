import uuid
from django.db import models
from django.contrib.auth import get_user_model
from vegetables.models import Vegetable
from markets.models import Market

User = get_user_model()

class Rate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    vegetable = models.ForeignKey(Vegetable, on_delete=models.CASCADE, related_name='rates')
    market = models.ForeignKey(Market, on_delete=models.CASCADE, related_name='rates')

    quantity = models.CharField(max_length=100)   # "10 kg", "100 bunches"
    price = models.DecimalField(max_digits=10, decimal_places=2)

    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='rates_added')
    verified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='rates_verified')

    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.vegetable.name} - {self.market.name} - {self.price}"
