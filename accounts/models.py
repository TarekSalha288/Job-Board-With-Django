from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=10)
    city=models.ForeignKey('City',on_delete=models.CASCADE,null=True,blank=True)
    @receiver(post_save, sender=User) 
    def create_profile(sender, instance, created, **kwargs):
      if created:
        Profile.objects.create(user=instance)
    def __str__(self):
        return str(self.user)     
class City (models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name   