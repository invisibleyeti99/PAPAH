from django.urls import path
from .views import formPageView,indexPageView
urlpatterns = [
    path('', indexPageView, name = 'index'), 
    path('form/', formPageView, name = 'form'),
]