from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'home.html')

def hobbies(request):
    return HttpResponse('<h1>Here will go my hobbies list.</h1>')