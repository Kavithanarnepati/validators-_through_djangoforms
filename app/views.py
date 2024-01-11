from django.shortcuts import render

# Create your views here.
from app.models import *
from app.forms import*
from django.http import HttpResponse

def create_school(request):
    ESFO=SchoolForm()
    d={'ESFO':ESFO}
    if request.method=='POST':
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            sn=SFDO.cleaned_data['Sname']
            sp=SFDO.cleaned_data['sprincipal']
            sl=SFDO.cleaned_data['slocation']
            e=SFDO.cleaned_data['email']
            res=SFDO.cleaned_data['renter_email']
            SO=School.objects.get_or_create(Sname=sn,sprincipal=sp,slocation=sl,email=e,renter_email=res)[0]
            SO.save()
            return HttpResponse('school is created')
        else:
            return HttpResponse('invalid data')
    return render(request,'create_school.html',d)






