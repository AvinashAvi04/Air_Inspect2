from django.db import models

from apps.user.models import Company


class Flight(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    fin = models.CharField(max_length=1024)
    model_name = models.CharField(max_length=1024)
    
    def __str__(self):
        return f"{self.company} {self.fin}"
