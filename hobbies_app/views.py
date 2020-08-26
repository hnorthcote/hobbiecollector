from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
class Hobby:
    def __init__(self, name, level, regularity = 'rarely' ):
        self.name = name
        self.level = level
        self.regularity = regularity


hobbies = [
    Hobby('Snowboard', 8, 'seasonal heavy'),
    Hobby('Biking', 5, 'seasonal rarely'),
    Hobby('Training', 8, 'year long steady'),
    Hobby('Computer assembly', 9, 'occasional'),
    Hobby('Traveling', 7, 'occasional'),
]

def home(request):
    return render(request,'home.html')

def hobbies_index(request):
    return render(request, 'hobbies/index.html', { 'hobbies': hobbies})