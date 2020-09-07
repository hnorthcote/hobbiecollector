from django.forms import ModelForm
from .models import Activity


class ActivityForm(ModelForm):
        class Meta:
                model = Friend
                fields = ['name', 'date']


