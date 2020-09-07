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
    path('hobbies/<int:hobby_id>/add_activity/', views.add_activity, name='activities_create'),
    path('hobbies/<int:hobby_id>/add_photo/', views.add_photo, name='add_photo'),
    path('friends/', views.friends_index, name='friends_index'),
    path('friends/create/', views.FriendCreate.as_view(), name='friends_create'),
    path('friends/<int:pk>/update/', views.FriendUpdate.as_view(), name='friends_update'),
    path('friends/<int:pk>/delete/', views.FriendDelete.as_view(), name='friends_delete'),
    path('activity/', views.activities_index, name='activities_index'),
    path('activity/<int:pk>/update/', views.ActivityUpdate.as_view(), name='activity_update'),
    path('activity/<int:pk>/delete/', views.ActivityDelete.as_view(), name='activity_delete'),
    path('accounts/signup/', views.signup, name='signup'),

]