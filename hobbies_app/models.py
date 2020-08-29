from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator
from django.urls import reverse

# Create your models here.
class Hobby(models.Model):
        name = models.CharField(max_length=150)
        level = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(0)])
        regularity = models.CharField(max_length=120)
        reason = models.CharField(max_length=500)
        active = models.BooleanField()  
##for function based views 
        def __str__(self):
            return self.name

## for class based views
        def get_absolute_url(self):
            return reverse('detail', kwargs={'hobby_id': self.id})

class Friend(models.Model):
    name = models.CharField(max_length=50)
    friendship = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('friends_index')