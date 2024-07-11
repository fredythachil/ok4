from django.shortcuts import render
from django.http import HttpResponse

from .models import Turf

# Create your views here. 

def index(request):
    return render(request,'index.html')

def home(request):
    dict_turf={
        'turf': Turf.objects.all()
    }
    return render(request,'home.html',dict_turf)
    
def profile(request):
    return render(request,'profile.html')
    
def contact(request):
    return render(request,'contact.html')

def register(request):
    return render(request,'reg.html')

def book(request):
    return render(request,'book.html')
    