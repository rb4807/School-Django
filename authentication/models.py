from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUser(AbstractUser):
    user_type_data=((1,"Principal"),(2,"Teacher"),(3,"Student"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)

class principal(models.Model) :
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    id=models.AutoField(primary_key=True)


class teacher(models.Model) :
    OPTIONS = (
        ('Teaching', 'Teaching 1'),
        ('Non Teaching', 'Teaching 2'),
    )
    name = models.CharField(max_length=50)
    image = models.FileField()
    dob = models.DateField()
    degree = models.CharField(max_length=50)
    experience = models.IntegerField()
    joined_no = models.DecimalField(max_digits=10, decimal_places=2)
    gender = models.CharField(max_length=50)
    field = models.CharField(max_length=100, choices=OPTIONS)
    handling = models.TextField(max_length=50)
    address = models.TextField()
    number = models.IntegerField()
    email = models.EmailField(max_length=254)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    id=models.AutoField(primary_key=True)




class student(models.Model) :
    OPTIONS = (
        ('A', 'A 1'),
        ('B', 'B 2'),
        ('C', 'C 3'),
        ('D', 'D 4'),
    )
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Student')
    dob = models.DateField()
    admission_no = models.DecimalField(max_digits=10, decimal_places=2)
    gender = models.CharField(max_length=50)
    std = models.IntegerField(choices=OPTIONS)
    division = models.CharField(max_length=100, choices=OPTIONS)
    teacher = models.CharField(max_length=50)
    address=models.TextField()
    f_name = models.CharField(max_length=50)
    f_occupation = models.CharField(max_length=50)
    f_number = models.IntegerField()
    m_name = models.CharField(max_length=50)
    m_occupation = models.CharField(max_length=50)
    m_number = models.IntegerField()
    guardian = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    id=models.AutoField(primary_key=True)

@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            principal.objects.create(admin=instance)
        if instance.user_type==2:
            teacher.objects.create(admin=instance,name="",image="",dob="1980-01-01",degree="",experience="1",joined_no="2",gender="",field="",handling="",address="",number="9",)
        if instance.user_type==3:
            student.objects.create(admin=instance,name="",dob="1980-01-01",teacher="", gender="", address="", admission_no="2", std="1", division="", f_name="", f_occupation="", f_number="9", m_name="", m_occupation="", m_number="9", guardian="")

@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.principal.save()
    if instance.user_type==2:
        instance.teacher.save()
    if instance.user_type==3:
        instance.student.save()