
from django.shortcuts import render,redirect
from django.urls import reverse 
from .models import Info
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
def send_message(request):
    info=Info.objects.first()
    if request.method=='POST':
         subject=request.POST['subject']
         messege=request.POST['message']
         email=request.POST['email']
         send_mail(subject,messege,email,[settings.EMAIL_HOST_USER])
         
          
          
          
        
    return render(request,'contact/contact.html',{"i":info})
