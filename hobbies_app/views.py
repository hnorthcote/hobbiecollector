from django.shortcuts import render
from django.http import HttpResponse
from .models import Hobby, Friend
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
#Hobbies function based views
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

# Hobbies Class based views

class HobbyCreate(CreateView):
  model = Hobby
  fields = '__all__'
class HobbyUpdate(UpdateView):
  model = Hobby
  fields = '__all__'
class HobbyDelete(DeleteView):
  model = Hobby
  success_url ='/hobbies/'


  ###########Friends area######

def friends_index(request):
    friends = Friend.objects.all()
    return render(request,'friends/index.html', {'friends': friends})


class FriendCreate(CreateView):
  model = Friend
  fields = '__all__' 
class FriendUpdate(UpdateView):
  model = Friend
  fields = "__all__"
class FriendDelete(DeleteView):
  model = Friend
  success_url ='/friends/'
