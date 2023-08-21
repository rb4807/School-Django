from django.urls import path
from . import views

urlpatterns = [
    path('student_list/',views.student_list,name='student_list'),
    path('student_form/',views.student_form,name='student_form'),
    path('student_detail',views.student_detail,name='student_detail'),
    path('add_student',views.add_student,name='add_student'),
    path('student/edit/<str:student_id>', views.student_edit, name='student_edit')


]

