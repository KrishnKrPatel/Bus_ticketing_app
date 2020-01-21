from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save,pre_save

class Address(models.Model):
    address_1 = models.CharField(max_length=250)
    address_2 = models.CharField(max_length=250,null=True,blank=True)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pincode = models.PositiveIntegerField()

    def __str__(self):
        return self.address_1

class Profile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    dob = models.DateField(null=True,blank=True)
    address = models.ForeignKey(Address,null=True,blank=True,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class BusRoute(models.Model):
    route = models.CharField(max_length=50)
    arrival_time = models.TimeField()
    departure_time = models.TimeField()

    def __str__(self):
        return self.route

class BusTimeTable(models.Model):
    time = models.TimeField()

    def __str__(self):
        return self.time


class Bus(models.Model):
    bus_name = models.CharField(max_length=50)
    bus_no = models.PositiveIntegerField()
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    bus_route = models.ManyToManyField(BusRoute)
    arrivial_time = models.TimeField()
    departure_time = models.TimeField()
    fare = models.DecimalField(max_digits=8,decimal_places=2)

    def __str__(self):
        return self.bus_name


BOOKING_STATUS=(
   ('C','Canceled'),
   ('B','Booked'),
   ('W','Watting')
)

FARE_CATEGORY=(
 ('C','Child'),
 ('A','Adult')
)

PAY_STATUS=(
('P','Pending'),
('F','Failed'),
('S','Success'),
)

class Booking(models.Model):
    cust_id = models.OneToOneField(Profile,on_delete=models.CASCADE)
    bus_id = models.OneToOneField(Bus,on_delete=models.CASCADE)
    status = models.CharField(blank=True,null=True,max_length=1,choices=BOOKING_STATUS)
    fare_category = models.CharField(max_length=1,choices=FARE_CATEGORY)
    fare = models.DecimalField(blank=True,null=True,max_digits=8,decimal_places=2,default=0.0)
    pay_status = models.CharField(max_length=1,choices=PAY_STATUS)

    def __str__(self):
        return "{} / {}".format(self.cust_id.user.first_name,self.bus_id.bus_name)



def pre_save_fare(sender,instance,**kwargs):
    if instance.fare_category == 'C':
        instance.fare = instance.bus_id.fare-25
    else:
        instance.fare = instance.bus_id.fare




pre_save.connect(pre_save_fare,sender=Booking)
