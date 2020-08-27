from django.shortcuts import render
from django.http import HttpResponse
from .models import Hobby

# Create your views here.

########################################
#####Before models class##################
# class Hobby:
#     def __init__(self, name, level, regularity = 'rarely' ):
#         self.name = name
#         self.level = level
#         self.regularity = regularity


# hobbies = [
#     Hobby('Snowboard', 8, 'seasonal heavy'),
#     Hobby('Biking', 5, 'seasonal rarely'),
#     Hobby('Training', 8, 'year long steady'),
#     Hobby('Computer assembly', 9, 'occasional'),
#     Hobby('Traveling', 7, 'occasional'),
# ]
##########################################################
def about(request):
    return render(request,'about.html')

def home(request):
    return render(request,'home.html')

def hobbies_index(request):
    hobbies = Hobby.objects.all()
    return render(request, 'hobbies/index.html', { 'hobbies': hobbies})

def hobbies_detail(request, hobby_id):
    hobby = Hobby.objects.get(id=hobby_id)
    return render(request, 'hobbies/detail.html', { 'hobby': hobby})

