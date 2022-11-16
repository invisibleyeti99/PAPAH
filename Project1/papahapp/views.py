from django.shortcuts import render
from django.http import HttpResponse

def indexPageView(request) : 
    return render(request, 'papahapp/index.html')
def formPageView(request) : 
     return render(request, 'papahapp/form.html')#28.08 on video
