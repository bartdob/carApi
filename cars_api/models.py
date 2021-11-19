import random
from django.db import models


def random_int():
    return random.randint(1, 5)


class Car(models.Model):
    make = models.CharField(max_length=25)
    model = models.CharField(max_length=25, default="")
    rank = models.IntegerField(default=random_int())

    def __str__(self):
        return self.make

    class Meta:
        verbose_name_plural = 'cars'

