from django.shortcuts import render
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import authenticate,login
from . models import Profile,City 
from . form import SignUpForm,ProfileForm,UserForm
# Create your views here.
def signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Update Sission
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect(reverse('accounts:profile'))
       
    
    else:
     form=SignUpForm()
    return render(request,'accounts/signup.html',{'f':form})
def profile(request):
    profile=Profile.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'p':profile})
def edit(request):
    profile=Profile.objects.get(user=request.user)
    if request.method=='POST':
          pf=ProfileForm(request.POST,request.FILES,instance=profile)
          uf=UserForm(request.POST,instance=request.user)
          if pf.is_valid() and uf.is_valid:
              uf.save()
              mypf=pf.save(commit=False)
              mypf.user=request.user
              mypf.save()
              return redirect(reverse('accounts:profile'))
    
    else:
        uf=UserForm(instance=request.user)
        pf=ProfileForm(instance=profile)    
    return render(request,'accounts/edit.html',{'u':uf,'p':pf})         
             

