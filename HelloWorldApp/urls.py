from django.contrib import admin
from django.urls import path, include
from .views import sayHello
 
urlpatterns = [
    path('', sayHello, name='sayHello')
]