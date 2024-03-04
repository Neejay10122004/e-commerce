from django.db import models

# Create your models here.
class contact_detail(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

class checkout_detail(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    compname = models.CharField(max_length=200)
    address = models.TextField()
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    pincode = models.CharField(max_length=6)
    mobile = models.CharField(max_length=10)
    emails = models.EmailField()