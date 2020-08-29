from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('hobbies/', views.hobbies_index, name='hobbies'),
    path('hobbies/<int:hobby_id>/', views.hobbies_detail, name='detail'),
    path('hobbies/create/', views.HobbyCreate.as_view(), name='hobbies_create'),
    path('hobbies/<int:pk>/update/', views.HobbyUpdate.as_view(), name='hobbies_update'),
    path('hobbies/<int:pk>/delete/', views.HobbyDelete.as_view(), name='hobbies_delete'),
    path('friends/', views.friends_index, name='friends_index'),
    path('friends/create/', views.FriendCreate.as_view(), name='friends_create'),
    path('friends/<int:pk>/update/', views.FriendUpdate.as_view(), name='friends_update'),
    path('friends/<int:pk>/delete/', views.FriendDelete.as_view(), name='friends_delete'),    

]