from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from authentication.models import student, CustomUser

def student_list(request):
    students=student.objects.all()
    return render(request,"teacher/student_list.html",{"students":students})

def student_form(request):
    return render(request,"teacher/student_form.html")

def student_detail(request):
    return render(request,"teacher/student_detail.html")

def student_edit(request,admin_id):
    students=students.objects.get(admin=student_id)
    return render(request, 'student_edit.html', {'students': students})

    # student=students.object.get(id=id)

def add_student(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        name = request.POST.get("name")
        image = request.POST.get("image")
        dob = request.POST.get("dob")
        admission_no = request.POST.get("admission_no")
        std = request.POST.get("std")
        division = request.POST.get("division")
        gender = request.POST.get("gender")
        teacher = request.POST.get("teacher")
        address = request.POST.get("address")
        f_name = request.POST.get("f_name")
        f_occupation = request.POST.get("f_occupation")
        f_number = request.POST.get("f_number")
        m_name = request.POST.get("m_name")
        m_occupation = request.POST.get("m_occupation")
        m_number = request.POST.get("m_number")
        guardian = request.POST.get("guardian")
        password = request.POST.get("password")
        email = request.POST.get("email")
        username = request.POST.get("username")
    try:
        user=CustomUser.objects.create_user(email=email,username=username,password=password,user_type=3)
        user.student.address=address
        user.student.name=name
        user.student.admission_no=admission_no
        user.student.std=std
        user.student.gender=gender
        user.student.division=division
        user.student.image=""
        user.student.dob=dob
        user.student.teacher=teacher
        user.student.f_name=f_name
        user.student.f_occupation=f_occupation
        user.student.f_number=f_number
        user.student.m_name=m_name
        user.student.m_occupation=m_occupation
        user.student.m_number=m_number
        user.student.guardian=guardian
        user.save()
        messages.success(request,"Successfully Added Student")
        return HttpResponseRedirect("/student_form")
    except:
        messages.error(request,"Failed to Add Student")
        return HttpResponseRedirect("/student_form")
