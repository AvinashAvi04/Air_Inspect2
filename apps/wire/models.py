from django.db import models

class WireFault(models.Model):
    fault_detected = models.BooleanField(default=False)
    component_name = models.CharField(max_length=255,null=True)
    fault = models.CharField(max_length=255,null=True)
    description = models.TextField(null=True)
    raw= models.TextField(null=True)