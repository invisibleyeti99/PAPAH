from django.shortcuts import render
from django.http import HttpResponse

def indexPageView(request) : 
    return HttpResponse("This is our main page")

def formPageView(request) : 
    return HttpResponse("This is our forms page")
