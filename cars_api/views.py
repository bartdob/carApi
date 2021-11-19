import requests
from django.shortcuts import render
from cars_api.forms import CarForm
from cars_api.models import Car
import os


def index(request):
    error_msg = ''
    message_class = ''  # css class
    message = ''  # msg for user

    url = 'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/%s?format=json'

    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            new_car = form.cleaned_data['make']
            new_model = form.cleaned_data['model']
            existing_car = Car.objects.filter(make=new_car).count()
            existing_model = Car.objects.filter(model=new_model).count()

        if (existing_car == 0 and existing_model == 0) or (existing_car == 1 and existing_model == 0):
            r_json = requests.get(url%(new_car))
            print(r_json)
            r = requests.get(url)
            model = res_json['Results'][0]['Model_Name']

            if r.status_code == 200:
                form.save()
            else:
                error_msg = "Car dont exist at all"

        else:
            error_msg = "Car alredy added"

        if error_msg:
            message = error_msg
            message_class = 'is-danger'
        else:
            message = 'City added successfully!!!'
            message_class = 'is-success'

    form = CarForm()

    context = {
        'form': form,
        'message': message,
        'message_class': message_class
    }

    return render(request, 'main.html', context)

# Create your views here.
