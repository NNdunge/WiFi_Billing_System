from asyncio.windows_events import NULL
from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.
class Sms_in(models.Model):
    sms_txt= models.CharField(max_length=50)
    sender_number = models.CharField(max_length=50)
    sent_dt = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return self.sms_txt ,self.sent_dt,self.sender_number


class Voucher_type(models.Model):
    voucherType= models.CharField(max_length=50)
    voucherPrice= models.IntegerField()
    validVoucherTime= models.IntegerField()

    def __str__(self):
        return self.voucherType,self.voucherPrice


class Voucher(models.Model):
    voucherID=models.CharField(primary_key=True, max_length=20)
    voucherType= models.ForeignKey(Voucher_type, on_delete=models.CASCADE)
    voucherStatus=models.SmallIntegerField(default=0)
    boughtTime= models.DateTimeField()
    generatedTime= models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.generatedTime,self.boughtTime,self.generatedTime


class Sms_out(models.Model):
    corresponding_request = models.ForeignKey(Sms_in, on_delete=models.CASCADE)
    currentTime_dt = models.DateTimeField(default=datetime.now())
    voucherID=models.ForeignKey(Voucher,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.corresponding_request,self.currentTime_dt,self.voucherID



