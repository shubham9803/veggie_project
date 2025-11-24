from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('collector', 'Collector'),
        ('viewer', 'Viewer'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='viewer')
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
