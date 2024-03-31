from django.shortcuts import render

# Create your views here.
def firstRender(request, *args, **kwargs):
    return render(request, 'frontend/index.html')