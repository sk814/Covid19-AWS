from django.shortcuts import render
from .models import Data

def home(request):
    obj =Data.objects.all()
    # context={
    #     obj.countryName,
    #     obj.coronaPositive,
    #     obj.death,
    # }

    return render(request, 'datapage.html',{'obj':obj})