from django.urls import path
from .views import *
urlpatterns = [
    path('', indexPageView, name = 'index'), 
    path('form/', formPageView, name = 'form'),
    path('delete/<str:pk>/', deletePageView, name = 'delete'),
    path('update/<str:pk>/', updatePageView, name = 'update')
]