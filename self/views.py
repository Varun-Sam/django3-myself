from django.shortcuts import render
from .models import Self



# Create your views here.
def home(request):
    projects = Self.objects.all()
    return render(request,'self/home.html', {'projects': projects})

def about(request):
    return render(request,'self/about.html')

