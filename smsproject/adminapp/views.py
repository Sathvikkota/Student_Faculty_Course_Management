from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

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

def admincourse(request):
    return render(request,"admincourse.html")

def adminstudent(request):
    return render(request,"adminstudent.html")

def adminfaculty(request):
    return render(request,"adminfaculty.html")

def addcourse(request):
    return render(request,"addcourse.html")

def insertcourse(request):
    if request.method=="POST":
        dept= request.POST["dept"]
        prog= request.POST["program"]
        ay= request.POST["ay"]
        sem= request.POST["sem"]
        year= request.POST["year"]
        ccode= request.POST["ccode"]
        ctitle= request.POST["ctitle"]

        course=Course(department=dept,program=prog,academicyear=ay,semester=sem,year=year,coursecode=ccode,coursetitle=ctitle)
        Course.save(course)

        msg="Course Added Successfully"

        return render(request,"addcourse.html",{"message":msg})

def deletecourse(request):
    courses=Course.objects.all()
    count = Course.objects.count()
    return render(request,"deletecourse.html",{"coursedata":courses,"count":count})

def coursedeletion(request,cid):

    Course.objects.filter(id=cid).delete()
    return redirect(deletecourse)   #deletecourse is a url name not based on html page name
    #return HttpResponse("Course Deleted Successfully")