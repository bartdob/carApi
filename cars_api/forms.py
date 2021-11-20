from django.forms import ModelForm, TextInput
from django import forms
from .models import Car, RATE_CHOICES, Review


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ('make', 'model')


class RateForm(ModelForm):
    rate = forms.CharField(widget=forms.Select(choices=RATE_CHOICES), required=True)

    class Meta:
        model = Review
        fields = ('rate', )

