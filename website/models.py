from django.db import models

# Create your models here.
class Response(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    message =models.CharField(max_length=1000)

    def __str__(self):
        return self.name
