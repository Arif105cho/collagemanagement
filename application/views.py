from django.shortcuts import render,redirect
from .models import CustomUser
from django.http import HttpResponse
from django.contrib import messages #import messages

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
