import uuid
from django.db import models

class Vegetable(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    marathi_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
