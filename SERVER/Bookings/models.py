from datetime import datetime

from django.db import models


# Create your models here.
class Cars(models.Model):
    name = models.CharField(max_length=250)
    model = models.CharField(max_length=250)
    year = models.DateField()
    image = models.ImageField(upload_to='Media/images/cars', blank=False, default='Media/bubble.png')
    slug = models.SlugField(unique=True)
    cc = models.CharField(max_length=100)
    transmission = models.CharField(max_length=250,default='Automatic')
    top_speed = models.CharField(max_length=250,default="260")
    load_capacity = models.IntegerField()
    pass_capacity = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    charge = models.FloatField()
    available = models.BooleanField(default=False)
    registration = models.CharField(max_length=250, default="KG")

    def __str__(self):
        return self.registration


class Rent(models.Model):
    first_name = models.CharField(max_length=250)
    second_name = models.CharField(max_length=250)
    id_no = models.IntegerField(default=0)
    telephone = models.IntegerField()
    # car = models.ForeignKey(Cars, on_delete=models.CASCADE, default='car')
    #model = models.SlugField(unique=True)
    registration = models.CharField(max_length=250, default="KG")
    period = models.CharField(max_length=100)
    from_date = models.DateField()
    to_date = models.DateField()
    payment = models.FloatField(default=0.0)
    picked = models.BooleanField(default=False)
    returned = models.BooleanField(default=False)
    remarks = models.TextField(default="Returned in Perfect Condition")

    def __str__(self):
        return '{} {} {} {} '.format(self.first_name, self.telephone, self.period,self.registration)
