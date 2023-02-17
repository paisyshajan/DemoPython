from django.http import HttpResponse
from django.shortcuts import render

from demoapp.models import Place


# Create your views here.
def home(request):
    placeobj=Place.objects.all()
    return render(request,'index.html',{'result1':placeobj})




# def operations(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     addition=x+y
#     subtraction=x-y
#     division=x/y
#     multipli=x*y
#     return render(request,'calculation.html',{'add':addition,'sub':subtraction,'div':division,'mul':multipli})










# def contact(request):
#     return HttpResponse("I am contact page")
# def details(request):
#     return render(request,'details.html')
# def thanks(request):
#     return HttpResponse("I am thanks page")