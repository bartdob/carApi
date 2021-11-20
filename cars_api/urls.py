from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<id>/', views.delete_car, name='delete_car'),
    path('rate/<id>/', views.rate_car, name='rate_car'),
]