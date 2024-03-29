# Storing the urls local to views.py
from django.urls import path
from .views import main

urlpatterns = [
    path('home/', main)
]