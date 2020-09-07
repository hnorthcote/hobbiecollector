from django.db import models
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
FRIENDSHIP_CHOICES = (("Old", "OLD FRIEND"), ("Close", "CLOSE FRIEND"), ("Good", "GOOD FRIEND"), ("New", "NEW FRIEND"),)

# Create your models here.
 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_color = models.CharField(max_length=50)


class Friend(models.Model):
    name = models.CharField(max_length=50)
    friendship = models.CharField(max_length=100, choices=FRIENDSHIP_CHOICES, default=FRIENDSHIP_CHOICES[3][0])

    def __str__(self):
        return self.name
    def get_absolute_url(self):
            return reverse('friends_index')

class Hobby(models.Model):
    name = models.CharField(max_length=150)
    level = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(0)])
    regularity = models.CharField(max_length=120)
    reason = models.CharField(max_length=500)
    active = models.BooleanField()
    friends = models.ManyToManyField(Friend)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail', kwargs={'hobby_id': self.id})
    def activities_for_hobby(self):
        return self.activity_set.filter(hobby=self.id)
## for class based views
 

class Activity(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField('activity date')
    hobby = models.ForeignKey(Hobby, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']


class Photo(models.Model):
    url = models.CharField(max_length=200)
    hobby = models.ForeignKey(Hobby, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for hobby_id: {self.hobby_id} @{self.url}"