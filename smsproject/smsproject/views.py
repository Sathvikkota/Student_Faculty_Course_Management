from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render


def demofunction(request):
    return HttpResponse("PROJECT")

def demofunction1(request):
    return HttpResponse("DEMO PAGE")

def demofunction2(request):
    return HttpResponse("<font color='orange'>STUDENT ACADEMIC MANAGEMENT SYSTEM</font>")

def homefunction(request):
    return render(request,"index.html")

def aboutfunction(request):
    return render(request,"about.html")

def loginfunction(request):
    return render(request,"login.html")

def contactfunction(request):
    return render(request,"contact.html")

