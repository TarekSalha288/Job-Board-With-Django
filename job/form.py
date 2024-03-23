from django import forms
from . models import Apply,Job
class JobApply(forms.ModelForm):
    class Meta:
        model=Apply
        fields=['name','email','cv','website','leter']
class AddJob(forms.ModelForm):
    class Meta:
        model=Job
        fields="__all__" 
        exclude=('slug','owner')       
        
