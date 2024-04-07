from django.db import models

class CityName(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
