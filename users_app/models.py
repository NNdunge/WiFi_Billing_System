from django.db import models
import uuid
from django.utils import timezone

# Create your models here.
class UserSignup(models.Model):
    GENDER = (
        ('M','Male'),
        ('F','Female')
    )
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=10,choices=GENDER)
    email = models.EmailField(unique=True)
    location=models.TextField(max_length=20)
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.firstName,self.lastName,self.dob,self.gender,self.email,self.location,self.status,self.created_at,self.updated_at

class VoucherRequest(models.Model):
    DEVICE = (
        ('Laptop','Laptop'),
        ('Mobile Phone','Mobile Phone')
    )
    VOUCHERTYPE = (
        ("pawa20", "pawa20"),
        ("pawa50", "pawa50"),
        ("pawa100", "pawa100"),
        ("wazito200", "wazito200"),
        ("boss500", "boss500"),
        ("GOAT1000", "GOAT1000")
        
    )
    amount=models.IntegerField()
    voucherType= models.CharField(max_length=20,choices=VOUCHERTYPE)
    voucherPrice= models.IntegerField()
    device=models.TextField(choices= DEVICE)

    def __str__(self):
        return self.amount,self.voucherType,self.voucherPrice,self.device

