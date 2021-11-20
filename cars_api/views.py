import requests
from django.shortcuts import render, redirect
from cars_api.forms import CarForm, RateForm
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
            new_car = form.cleaned_data['make'].lower()
            print(new_car)
            new_model = form.cleaned_data['model']
            # existing_car = Car.objects.filter(make=new_car).count()
            # existing_model = Car.objects.filter(model=new_model).count()

        # if (existing_car == 0 and existing_model == 0) or (existing_car == 1 and existing_model == 0):
            r_json = requests.get(url%(new_car)).json()
            r = requests.get(url)
            model = r_json['Results'][0]['Model_Name']
            make = r_json['Results'][0]['Make_Name'].lower()
            print(make)
            # new_model = form.cleaned_data['model']

            if r.status_code == 200 and make == new_car:
                form.save()
            else:
                error_msg = "Car dont exist at all"

        # else:
        #     error_msg = "Car alredy added"

        if error_msg:
            message = error_msg
            message_class = 'is-danger'
        else:
            message = 'Car added successfully!!!'
            message_class = 'is-success'

    form = CarForm()

    cars = Car.objects.all()



    context = {
        'cars': cars,
        'form': form,
        'message': message,
        'message_class': message_class
    }

    return render(request, 'main.html', context)

def rate_car(request, id):
    car = Car.objects.get(id=id)

    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.car = car
            rate.save()


    return redirect('index')



def delete_car(request, id):
    Car.objects.get(id=id).delete()

    return redirect('index')

# Create your views here.
