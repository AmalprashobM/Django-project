from django.http.request import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from .models import createuser
#from twilio.rest import Client
#from .models import AuthorizedDevice, Profile, TwoFAToken, TWOFAVerified
#from helpers import random_str
import os

# Create your views here.
def register(request):
    if request.method =="POST":
        fname = request.POST["rname"]
        
        email = request.POST["rmail"]
        
        phone = request.POST["rphone"]
        password = request.POST["rpswd"]
        role = request.POST["role"]
        User.objects.create_user(username=email, email=email, first_name=fname, password=password).save()
        createuser(userid=email,role=role).save()
        return HttpResponseRedirect("/auth/login/")
        
    else:
        return render(request, "authentication/register.html")

def loginop(request):
    
    if request.method =="POST":
        email = request.POST["lmail"]
        password = request.POST["lpswd"]
        user = authenticate(username=email, password=password)
        usertype = createuser.objects.get(userid=email)
        print(usertype.role)

        
        if user is not None:
            login(request,user)
            if usertype.role == 'Seller':
                return HttpResponseRedirect("/seller/")
            else:
                return render(request,"shopper/index.html")
            
             
            
            
        else:
            return HttpResponse("Wrong credentials")    
    else:
        return render(request, "authentication/login2.html")

    
def logoutop(request):
    logout(request)
    return render(request, "authentication/login2.html")