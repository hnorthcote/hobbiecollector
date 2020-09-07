from django.contrib import admin
from .models import Hobby, Photo, Friend, Activity

# Register your models here.
admin.site.register(Hobby)
admin.site.register(Photo)
admin.site.register(Friend)
admin.site.register(Activity)