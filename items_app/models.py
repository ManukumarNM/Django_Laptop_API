from django.db import models

# Create your models here.
class LaptopsModel(models.Model):
    name = models.CharField(max_length=20, blank=False)
    brand = models.CharField(max_length=20, blank=False)
    price = models.IntegerField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"