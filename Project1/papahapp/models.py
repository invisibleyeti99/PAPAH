from django.db import models

# Create your models here.

#This stuff will be changed a bit to be part of the database Papah

# from django.db import models
# from datetime import datetime, timedelta

# # Create your models here.
# class TripCategory(models.Model):
#     description = models.CharField(max_length=20)

#     def __str__(self) :
#         return (self.description)

# class Destination(models.Model) :
#     trip_category = models.OneToOneField(TripCategory, models.CASCADE)
#     title = models.CharField(max_length=50)
#     days = models.IntegerField(default=0)
#     cost = models.DecimalField(max_digits=8, decimal_places=2) 
#     main_photo = models.ImageField(upload_to='photos')          
#     is_active = models.BooleanField(default=True)
#     leave_date = models.DateField(default=datetime.today, blank=True)

#     def __str__ (self):
#         return (self.title)

#     @property
#     def return_date(self) :
#         return (self.leave_date + timedelta(days=self.days))

# class Customer(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     user_name = models.CharField(max_length=20)
#     password = models.CharField(max_length=20)
#     email = models.EmailField(max_length=100)    
#     phone = models.CharField(max_length=13, blank=True)
#     destinations = models.ManyToManyField(Destination, blank=True)

#     def __str__(self):
#         return (self.full_name)

#     @property
#     def full_name(self):
#         return '%s %s' % (self.first_name, self.last_name)

#     #override the save method
#     def save(self):
#         self.first_name = self.first_name.upper()
#         super(Customer, self).save() # Call the "real" save() method.
