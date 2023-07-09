
from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    print("test function is called from view")
    return render(request,"home.html")