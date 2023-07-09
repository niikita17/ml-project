from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
  path('',views.registration, name="registration"),
    path('result',views.result,name="result"),
  #  path("register/",student_register),
 
]
