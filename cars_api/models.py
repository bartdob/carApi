from django.db import models


class Car(models.Model):
    make = models.CharField(max_length=25)
    model = models.CharField(max_length=25, default="")
    rank = models.IntegerField(default=1)

    def __str__(self):
        return self.make

    class Meta:
        verbose_name_plural = 'cars'

