from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *

def indexPageView(request) : 

    return render(request, 'papahapp/index.html')

def formPageView(request) : 
    data = Breach.objects.all()
    if request.method == 'POST':
        form = BreachForm(request.POST,)
        if form.is_valid():
            form.save()
    else:
        form = BreachForm()
        context = {
        'data': data,
        'form': form,

    }
   
        return render(request, 'papahapp/form.html', context)#28.08 on video

