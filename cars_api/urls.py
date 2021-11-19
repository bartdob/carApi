from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<car_model>/', views.delete_car, name='delete_car'),
]