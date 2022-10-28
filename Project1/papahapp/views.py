from django.shortcuts import render
from django.http import HttpResponse

def indexPageView(request) : 
    return HttpResponse("This is our main page talking about Phishing and Hacking")

def formPageView(request) : 
    return HttpResponse("Forms")
