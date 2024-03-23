from django.db import models

# Create your models here.
class Info(models.Model):
    city=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    def __str__(self):
        return self.email