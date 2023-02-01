from django.contrib import admin
from django.urls import path, include
from main import views
from django.http import HttpResponse

urlpatterns = [
    path('', views.index),
    path('vxod2', views.vxod2),
    path('index', views.index),
]