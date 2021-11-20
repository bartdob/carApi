import random
from django.db import models


# def random_int():
#     return random.randint(1, 5)


class Car(models.Model):
    make = models.CharField(max_length=25)
    model = models.CharField(max_length=25, default="")

    def __str__(self):
        return self.make

    def __str__(self):
        return self.model

    class Meta:
        verbose_name_plural = 'cars'


RATE_CHOICES = [
    (1, '1-Trash'),
    (2, '2 - Horrible'),
    (3, '3 - OK'),
    (4, '4 - GOOD'),
    (5, '5 - PERF'),

]


class Review(models.Model):
    car = models.ForeignKey(Car, null=True, on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)

    def __str__(self):
        return "%s %s" % (self.car.make, self.car.model)


