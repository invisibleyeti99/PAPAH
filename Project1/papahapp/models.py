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

class Breach(models.Model) :
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    breach_num = models.IntegerField(default=0)
    street_address = models.CharField(max_length = 100)
    apt_number = models.CharField(max_length = 5) 
    city = models.CharField(max_length = 80)
    state_abbreviation = models.CharField(max_length = 2)
    zipcode = models.IntegerField(default=0)
    email = models.EmailField()          
    phone = models.CharField(max_length=10)
    breach_type = models.CharField(max_length=20)
    breach_description = models.CharField(max_length = 1000)
    breach_datetime = models.DateTimeField()

    def __str__(self):
                    return (self.full_name)
                
    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)
    
    def save(self):
        self.first_name = self.first_name.upper()
        self.last_name = self.last_name.upper()
        self.street_address = self.street_address.upper()
        self.city = self.city.upper()
        self.state = self.state.upper()
        self.email = self.email.upper()
        self.breach_type = self.breach_type.upper()
        super(Breach, self).save() # Call the "real" save() method

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
