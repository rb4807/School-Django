from django.urls import path
from . import views

urlpatterns = [
    path('teacher_form/',views.teacher_form,name='teacher_form'),
    path('add_teacher',views.add_teacher,name='add_teacher'),
    path('teacher',views.teacher,name='teacher'),
    path('teacher_list/',views.teacher_list,name='teacher_list'),

]