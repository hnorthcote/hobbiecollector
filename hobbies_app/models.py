from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator

# Create your models here.
class Hobby(models.Model):
        name = models.CharField(max_length=150)
        level = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(0)])
        regularity = models.CharField(max_length=120)
        reason = models.CharField(max_length=500)
        active = models.BooleanField()   
        def __str__(self):
            return self.name