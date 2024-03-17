from django.db import models

# Create your models here.


class Reservation(models.Model):
    Choices = (('1', '1'),
               ('2', '2'),
               ('3', '3'),
               ('4', '4'),
               ('5', '5'),)
    full_name = models.CharField(max_length=100, verbose_name="")
    phone = models.CharField(max_length=20, verbose_name="")
    email = models.EmailField(verbose_name="")
    person_Count = models.CharField(max_length=10, choices=Choices, default='1', verbose_name="")
    date = models.DateField(verbose_name="")

    def __str__(self):
        return self.name + ' : ' + str(self.date)
