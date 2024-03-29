import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from authentication.EmailBackEnd import EmailBackEnd


def user_login(request):
    return render(request,"authentication/login.html")

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type=="1":
                return HttpResponseRedirect('/principal')
            elif user.user_type=="2":
                return HttpResponse("teacher")
            else:
                return HttpResponse("student")
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/")

def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("User : "+request.user.username+" usertype : "+str(request.user.user_type))
    else:
        return HttpResponse("Please Login First")

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/login")

