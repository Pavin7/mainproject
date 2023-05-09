from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def fun(request):
    return render(request,"index.html")

def abt(request):
    return render(request,"about.html")

