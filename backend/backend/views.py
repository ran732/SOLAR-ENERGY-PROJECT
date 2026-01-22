from django.http import HttpResponse
from django.shortcuts import render

def page(request):
    return HttpResponse ("hello world")

def homepage(request):
    return render (request, "index.html")