from django.shortcuts import render
from django.http import HttpResponse

def indexPageView(request) : 
    return HttpResponse("This is our main page")

def formPageView(request) : 
    return HttpResponse("This is a page with the form that people can fill out to report phishing.")
