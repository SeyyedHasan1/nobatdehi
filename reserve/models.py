from re import T
from django.db import models
# Create your models here.




class Doctor(models.Model):
    capacity= models.IntegerField(blank =True, null=True)


    def __str__(self):
        return str(self.capacity)


class Reservation(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    doctorid = models.IntegerField(blank=True, null=True, default=1, editable=False)
    capacity = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank = True)

    def __str__(self):
        return str(self.doctorid)


