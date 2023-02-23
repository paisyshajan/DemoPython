from django.http import HttpResponse
from django.shortcuts import render
from .models import  Place,Team
# Create your views here.
def demo(request):
   placeobj=Place.objects.all()
   teamobj=Team.objects.all()
   return render(request,"index.html",{'result1':placeobj,'result2':teamobj})


# def register(request):
#    return render(request,'register.html')









# def addition(request):
#    x=int(request.GET['num1'])
#    y=int(request.GET['num2'])
#    res=x+y
#    return render(request,'aditionpage.html',{'result':res})



# def about(request):
#    return render(request,'about.html')
#
# def contact(request):
#       return HttpResponse("i am contact")

   #return HttpResponse("helloo world")

