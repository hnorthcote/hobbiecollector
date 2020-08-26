from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hobbies/', views.hobbies_index, name='hobbies'),

]