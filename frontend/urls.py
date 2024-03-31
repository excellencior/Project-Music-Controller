from django.urls import path
from .views import firstRender

urlpatterns = [
    path('', firstRender)
]