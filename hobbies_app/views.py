from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Hobby, Friend, Activity, Photo
from .forms import ActivityForm
import uuid
import boto3
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


S3_BASE_URL = "https://hobby-collector.s3.amazonaws.com/"
BUCKET = ""

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

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('hobbies')
    else:
      error_message = 'Invalid sign up, try again!'
  form = UserCreationForm()
  context = {'form' : form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

@login_required
def add_photo(request, hobby_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
       
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{key}"
            photo = Photo(url=url, hobby_id=hobby_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', hobby_id=hobby_id)


def about(request):
    return render(request,'about.html')

def home(request):
    return render(request,'home.html')

@login_required
def hobbies_index(request):
    hobbies = Hobby.objects.all()
    return render(request, 'hobbies/index.html', { 'hobbies': hobbies})

@login_required
def hobbies_detail(request, hobby_id):
    hobby = Hobby.objects.get(id=hobby_id)
    friends_not_related = Friend.objects.exclude(id__in=hobby.friends.all().values_list('id'))
    activity_form = ActivityForm()
    return render(request, 'hobbies/detail.html', { 'hobby': hobby, 'activity_form': activity_form, 'friends': friends_not_related,},)


# Hobbies Class based views

class HobbyCreate(LoginRequiredMixin, CreateView):
  model = Hobby
  fields = ['name', 'level', 'regularity', 'reason','active','friends']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
class HobbyUpdate(LoginRequiredMixin, UpdateView):
  model = Hobby
  fields = ['name', 'level', 'regularity', 'reason','active','friends']
class HobbyDelete(LoginRequiredMixin, DeleteView):
  model = Hobby
  success_url ='/hobbies/'


  ###########Friends area######


@login_required
def friends_index(request):
    friends = Friend.objects.all()
    return render(request,'friends/index.html', {'friends': friends})

@login_required
def relate_friend(request, hobby_id, friend_id):
  Hobby.objects.get(id=hobby_id).friends.add(friend_id)
  return redirect('detail', hobby_id=hobby_id)
@login_required
def disconnect_friend(request, hobby_id, friend_id):
  Hobby.objects.get(id=hobby_id).friends.remove(friend_id)
  return redirect('detail', hobby_id=hobby_id)

class FriendCreate(LoginRequiredMixin, CreateView):
  model = Friend
  fields = ['name', 'friendship']
class FriendUpdate(LoginRequiredMixin, UpdateView):
  model = Friend
  fields = ['name', 'friendship']
class FriendDelete(LoginRequiredMixin, DeleteView):
  model = Friend
  success_url ='/friends/'


########Activities Area

def activities_index(request):
  activities = Activity.objects.all()
  return render(request,'activities/index.html', {'activities' : activities})

def add_activity(request, hobby_id):
  form  = ActivityForm(request.POST)

  if form.is_valid():
    new_activity = form.save(commit=False)
    new_activity.hobby_id=hobby_id
    new_activity.save()
  return redirect('detail', hobby_id=hobby_id)

class ActivityUpdate(LoginRequiredMixin, UpdateView):
  model = Activity
  fields = ['name', 'date']

class ActivityDelete(LoginRequiredMixin, DeleteView):
  model = Activity
  success_url ='/activities/'


