from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def user_login(request):
    if request.method=="GET":
        return render(request,'accounts/login.html')
    else:
        iname=request.POST['iname']
        ipass=request.POST['ipass']

        if iname=='' or ipass=='':
            return render(request,'accounts/login.html',{'errmsg':"Username or Password cannot be blank!"})
        else:
            u=authenticate(username=iname,password=ipass)
            if u is not None:
                login(request,u)
                return redirect('/')
            else:
                return render(request,'accounts/login.html',{'errmsg':"Invalid Username or Password"})
            
def user_logout(request):
    logout(request)
    return redirect('/')

def user_register(request):
    if request.method=="GET":
        return render(request,'accounts/register.html')
    else:
        iname=request.POST['iname']
        iemail=request.POST['iemail']
        ipass=request.POST['ipass']
        cipass=request.POST['cipass']

        if iname=='' or iemail=='' or ipass=='' or cipass=='':
            return render(request,'accounts/register.html',{'errmsg':"Fields cannot be blank!"})
        elif len(ipass)<8:
            return render(request,'accounts/register.html',{'errmsg':"Password must be 8 characters or more!"})
        elif ipass.isdigit():
            return render(request,'accounts/register.html',{'errmsg':"Password cannot be entirely in digits!"})
        elif ipass!=cipass:
            return render(request,'accounts/register.html',{'errmsg':"Password does not match!"})
        else:
            u = User.objects.create(username=iname,email=iemail,password=ipass)
            u.set_password(ipass)
            u.save()
            return render(request,'accounts/register.html',{'errmsg':"User created successfully!"})