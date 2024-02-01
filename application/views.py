from django.shortcuts import render,redirect
from .models import CustomUser
from django.http import HttpResponse
from django.contrib import messages #import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password

# Create your views here.

def HeaderView(request):
    return render(request,"header.html")


def ProfessorView(request):
    if request.method == "POST" or request.method == "FILES":
        username = request.POST.get('username')
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        image = request.FILES['image'] 
        password = request.POST.get("passs")
        print("details -- ",username,fname, phone, email,image)
        user = CustomUser.objects.create(username=username,first_name=fname,last_name=lname,phone=phone,email=email,is_staff=True,profile=image)
        user.set_password(password)
        user.user_type = "professor"
        user.save()
        messages.success(request, "Data Saved Success." )
        return redirect("header")

    return render(request,"professor.html")


def ProfessorListView(request):
    stud = CustomUser.objects.filter(user_type = "student")
    prof = CustomUser.objects.filter(user_type="professor")
    return render(request,"AllList.html",{"profs":prof,"studs":stud}) # dict['profs'] =return krega all records from customerUSer table


def loginView(request):
    # user = CustomUser.objects.get(id=6)
    # user.password=make_password(user.password) # import hash password /make_password from django inbullt
    # user.save()
    print("method name- ",request.method)
    if request.method == 'POST':
        username = request.POST.get('username')
        password=request.POST.get("password")
        print("details ",username,password)
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect("header")
        else:
            return render(request,"login.html")

    return render(request,"login.html")



def getProfessor(request):
    user = CustomUser.objects.get(username = request.user)
    print("user-- ",user)
    return render(request,"home.html",{"user":user})