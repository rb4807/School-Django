from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.user_login,name='login'),
    path('doLogin',views.doLogin,name='doLogin'),
    path('get_user_details', views.GetUserDetails),
    path('logout/', views.user_logout,name='logout'),

]