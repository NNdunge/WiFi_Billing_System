import re
from asyncio.windows_events import NULL
from types import NoneType
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.utils.crypto import get_random_string
from django.shortcuts import render,redirect

from django.forms import ValidationError
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from .forms import CreateUserForm
from .models import *

# Create your views here.

   
@csrf_exempt
def smsInbox(request):
   if request.method == "POST":
      sms_txt = request.POST.get('text')
      sender_number = request.POST.get('sender')
      sent_dt = request.POST.get('sc_datetime')

      #save in new data in database,table->sms_in
      new_sms = Sms_in(sms_txt=sms_txt, sender_number=sender_number, sent_dt=sent_dt)
      new_sms.save()
      
      #get amount of amount from sms_txt
      searchObj= re.search(r'(\d*\.?\d+|\d{1,3}(,\d{3})*(\.\d+)?)',sms_txt,flags=0)
      #[\W](\d*|\d{0,2}(,\d{3})*[0-9]+
      amount = 0
      voucherID=NULL
      if searchObj:
            amount =float(searchObj.group().replace(',', '')) 
            print ("Amount----->" ,amount)
            
            #Check if amount exists, and obtain the voucher typeID
            if amount > 0:
               for typeID in Voucher_type.objects.all():
                  if typeID.voucherPrice == amount:
                     #function call to retrieveVoucher
                     voucherID = retrieveVoucher(amount)
                     if voucherID == NULL:
                        voucherID =generateVoucher(typeID)
                     if voucherID == NULL:
                        voucherID ='issueGen'
                     break
               
            #If voucher type does NOT exist then return null 
            if voucherID == NULL:
               voucherID = 'TypeDNE'  
      else:
         voucherID='sendAmount'

      sentID=Voucher.objects.get(voucherID=voucherID)
      sms_out = Sms_out(corresponding_request=new_sms, currentTime_dt=datetime.now(),voucherID=sentID)
      sms_out.save()

      return HttpResponse(voucherID)

   else:
      sms_db = Sms_in.objects.all()
      context = {'sms_db':sms_db}
      return render(request, 'sms_app/index.html',context)


def generateVoucher(type_ID):   
   #Generation of voucherID...   
   retrievedID=NULL
   for i in range(1,15) :
      generatedID = get_random_string(length=10)
      #Check if the generated id already exists
      try:
         Voucher.objects.get(voucherID=generatedID)
      except Voucher.DoesNotExist:
         #Save if it doesnt exist
         newID=Voucher(voucherID=generatedID,voucherType=type_ID)
         if retrievedID==NULL:
            retrievedID=generatedID
            newID.voucherStatus=1
            newID.boughtTime=datetime.now()
         newID.save()

   return retrievedID


def retrieveVoucher(price):
   #Check for unused vouchers of the paid price in voucher table 
   #Join the voucher and voucher_type table based on common voucher_type
   voucherID = NULL
   for object in Voucher.objects.select_related('voucherType'):
      if object.voucherType.voucherPrice==price and object.voucherStatus==0:
         voucherID=object.voucherID
         print('Found ID: ' + voucherID)
         #if there are valid unused vouchers pick one and mark it as bought(Update Voucher table)
         mark=Voucher.objects.get(voucherID=voucherID)
         mark.voucherStatus=1
         mark.boughtTime=datetime.now()
         mark.save()
         break
                   
   return voucherID
          
def register(request):
       form = CreateUserForm()

       if request.method == 'POST':
              form = CreateUserForm(request.POST)
              #Validate form
              if form.is_valid():
                     form.save()
                     username= form.cleaned_data.get('username')
                     password =form.cleaned_data.get('password')
                     user= authenticate(username=username,password=password)
                     login(request,user)
            
       context={'form':form}
       return render (request,'sms_app/authentication/register.html',context)

def signIn(request):
       context={}
       return render(request,'sms_app/authentication/signin.html',context)

def forgotPass(request):
       context={}
       return render(request,'sms_app/authentication/forgot-password.html',context)

def checkEmail(request):
       context={}
       return render(request,'sms_app/authentication/check-email.html',context)



            

      

   

 
      
         




          