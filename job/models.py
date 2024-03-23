from django.db import models
from django.contrib.auth.models import User
# Create your models here.
types=(
    ('Full Time','Full Time'),
    ('Part Time','Part Time')
)


class Job(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    job_type=models.CharField(max_length=15,choices=types)
    descreption=models.TextField(max_length=1000)
    published_At=models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experience=models.IntegerField(default=1)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
    slug=models.SlugField(blank=True,null=True)
    def save(self,*args,**kwargs):
        self.slug=self.title
        super(Job,self).save(*args,**kwargs)
    def __str__(self) :
        return self.title 
class Apply(models.Model):
    job=models.ForeignKey(Job,on_delete=models.CASCADE)
    name=models.CharField(max_length=25)
    email=models.EmailField()
    leter=models.TextField(max_length=150)
    cv=models.FileField(upload_to="uploads/")
    website=models.URLField()
    created_At=models.DateTimeField(auto_now=True)
    def __str__(self) :
        return self.name 
class Category(models.Model) :
    name=models.CharField(max_length=20)
    def __str__(self) :
        return self.name 
