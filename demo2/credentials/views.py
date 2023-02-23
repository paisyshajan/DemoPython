from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
def login (request):
    if request.method=='POST':
        usrnme=request.POST['username']
        passwrd=request.POST['password']
        user=auth.authenticate(username=usrnme,password=passwrd)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid user')
            return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.method== 'POST':
        Usrnme = request.POST['username']    #Usrname is variable, username is name that in the <input>
        Email = request.POST['email']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        passw = request.POST['password']
        cpassword = request.POST['cpassword']

        if passw==cpassword: #password verification
            if User.objects.filter(username=Usrnme).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=Email).exists():
                messages.info(request, "email takes")
                return redirect('register')
            else:
              user=User.objects.create_user(username=Usrnme,email=Email,password=passw,first_name=fname,last_name=lname,)
              user.save();
              print("user created")
              return redirect('login')
              messages.info(request,"user saved")
        else:
            messages.info(request,"password not matching")
            return redirect('register')
            # print("password not matching")
        return redirect('/')
    return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')