from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *

def indexPageView(request) : 
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
        #'breachs' : breachs,
    }
    return render(request, 'papahapp/index.html',context)


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
        #'breachs' : breachs,
    }
    return render(request, 'papahapp/form.html', context)

def deletePageView(request, pk):
    breach = Breach.objects.get(id=pk)
    if request.method == 'POST':
        breach.delete()
        return redirect('index')
    context = {'item' : breach}
    return render(request, 'papahapp/delete.html', context)
