
from django import forms



def validtae_for_d(data):
    if data[0].startswith('d'):
        raise forms.ValidationError('starts with d')
    


def  validate_for_len(data):
    if len(data)<5:
        raise forms.ValidationError('len is lessthan 5')
    
from app.models import *
class SchoolForm(forms.Form):
    Sname=forms.CharField(validators=[validtae_for_d,validate_for_len])
    sprincipal=forms.CharField()
    slocation=forms.CharField()
    email=forms.EmailField()
    renter_email=forms.EmailField()



    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['renter_email']
        if e!=re:
            raise forms.ValidationError('email does not matched')

