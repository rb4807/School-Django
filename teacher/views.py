from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from authentication.models import teacher, CustomUser

def teacher_form(request):
    return render(request,"principal/teacher_form.html")

def teacher(request):
    return render(request,"principal/teacher.html")

def add_teacher(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        name = request.POST.get("name")
        image = request.POST.get("image")
        dob = request.POST.get("dob")
        degree = request.POST.get("degree")
        experience = request.POST.get("experience")
        joined_no = request.POST.get("joined_no")
        gender = request.POST.get("gender")
        field = request.POST.get("field")
        address = request.POST.get("address")
        handling = request.POST.get("handling")
        number = request.POST.get("number")
        email = request.POST.get("email")
        password = request.POST.get("password")
        username = request.POST.get("username")
        try:
            user=CustomUser.objects.create_user(username=username,password=password,email=email,user_type=2)
            user.teacher.address=address
            user.teacher.name=name
            user.teacher.number=number
            user.teacher.handling=handling
            user.teacher.gender=gender
            user.teacher.field=field
            user.teacher.image=""
            user.teacher.dob=dob
            user.teacher.degree=degree
            user.teacher.experience=experience
            user.teacher.joined_no=joined_no
            user.save()
            messages.success(request,"Successfully Added Staff")
            return HttpResponseRedirect("/teacher_form")
        except:
            messages.error(request,"Failed to Add Staff")
            return HttpResponseRedirect("/teacher_form")

def teacher_list(request):
    teachers =teacher.objects.all()
    return render(request,"principal/teacher_list.html",{"teachers":teachers})