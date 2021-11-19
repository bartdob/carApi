from django.forms import ModelForm, TextInput
from .models import Car


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ('make', 'model')
