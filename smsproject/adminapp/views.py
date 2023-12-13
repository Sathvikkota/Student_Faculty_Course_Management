from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from .models import Admin, Student, Course, Faculty


# Create your views here.
def adminhome(request):
    return render(request,"adminhome.html")


def logout(request):
    return render(request,"login.html")

def checkadminlogin(request):
    adminuname=request.POST["uname"]
    adminpwd=request.POST["pwd"]

    flag=Admin.objects.filter(Q(username=adminuname)&Q(password=adminpwd))
    print(flag)

    if flag:
        return render(request,"adminhome.html")
    else:
        return HttpResponse("Login Failed")

def viewstudents(request):
    students=Student.objects.all()
    count=Student.objects.count()
    return render(request,"viewstudents.html",{"studentdata":students,"count":count})

def viewcourses(request):
    courses=Course.objects.all()
    count = Course.objects.count()
    return render(request,"viewcourses.html",{"coursedata":courses,"count":count})

def viewfaculty(request):
    faculty=Faculty.objects.all()
    count = Faculty.objects.count()
    return render(request,"viewfaculty.html",{"facultydata":faculty,"count":count})
