from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
class Data(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()


    def __str__(self):
        return self.title

class NewTodo(models.Model):
    title = models.CharField(max_length=200)
    
    text = models.TextField()
    created_on = models.DateTimeField(default=datetime.datetime.now())
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' | ' + self.created_by.username


class HotelBooking(models.Model):
    name = models.CharField(max_length=200)
    booking_details = models.TextField(max_length=200)
    booked_on = models.DateTimeField(default=datetime.datetime.now())
    booked_by = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return self.name + '|' + self.booked_by.username

