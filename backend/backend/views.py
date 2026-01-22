from django.http import HttpResponse
from django.shortcuts import render

def page(request):
    return HttpResponse ("hello world")

def homepage(repuest):
    return render (repuest, "index.html")