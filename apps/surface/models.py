from django.db import models
from apps.flight.models import Flight


class SurfaceDamage(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, null=True, blank=True)
    repair_status = models.BooleanField(default=False)
    damage_type = models.CharField(max_length=1024)
    level = models.CharField(max_length=1024)
    part = models.CharField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to='surface_damage/main/', null=True, blank=True)
    metadata = models.JSONField(default=None, null=True, blank=True)
