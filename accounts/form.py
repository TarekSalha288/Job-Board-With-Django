from django import forms
from . models import Profile,City
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class SignUpForm(UserCreationForm):
    class  Meta:
        model=User
        fields=['username','email']
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']             
class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['phone','city']


