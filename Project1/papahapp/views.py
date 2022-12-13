from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *

def indexPageView(request) : 
    data = Breach.objects.all()
    #breachs = request.user.breachs_set.all() dunno why this isn't working, but we have to define breach to be able to use it in the context
    if request.method == 'POST':
        form = BreachForm(request.POST,)
        if form.is_valid():
            form.save()
    else:
        form = BreachForm()
    context = {
        'data': data,
        'form': form,
        #'breachs' : breachs,
    }
    return render(request, 'papahapp/index.html')


def formPageView(request) : 
    data = Breach.objects.all()
    #breachs = request.user.breachs_set.all() dunno why this isn't working, but we have to define breach to be able to use it in the context
    if request.method == 'POST':
        form = BreachForm(request.POST,)
        if form.is_valid():
            form.save()
    else:
        form = BreachForm()
    context = {
        'data': data,
        'form': form,
        #'breachs' : breachs,
    }
    return render(request, 'papahapp/form.html', context)

