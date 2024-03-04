from django import forms
from .models import contact_detail
from .models import checkout_detail

class ContactDetailForm(forms.ModelForm):
    class Meta:
        model = contact_detail
        fields = ['name', 'email', 'message']

class CustomerDetailForm(forms.ModelForm):
    class Meta:
        model = checkout_detail 
        fields = ['firstname','lastname','compname','address','city','country','pincode','mobile','emails']