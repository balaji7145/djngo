from .models import FormModel
from django import forms 
class Form(forms.ModelForm):
    class Meta:
        model = FormModel
        fields =('name','age','address')