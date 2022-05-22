from fnmatch import fnmatch
from http import HTTPStatus
from .forms import MyUser
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib import messages
from datetime import datetime

#new imports here
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages



# Create your views here.
def register(request):
    form = MyUser()
    if request.method == 'POST':
        form = MyUser(request.POST)
        #Validate form
        if form.is_valid():
            print(request.POST)
            form.save()

            login(request,MyUser)
            return redirect('home')
        else:
            context={'form':form}  
            all_errors = form.errors.as_data()
            for err in all_errors:
                print(err) 
            return render (request,'users_app/user_authentication/userRegister.html',context)
            
    else:     
        context={'form':form}             
        return render (request,'sms_app/user_authentication/userRegister.html',context)

def signIn(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user_to_be_authenticated = authenticate(username=username,password=password)
        if user_to_be_authenticated is not None:      
            login(request,user_to_be_authenticated) 
            return redirect('home')
        else:
            messages.info(request,"Sorry wrong credentials")
    context={}
    return render(request,'users_app/user_authentication/userSignin.html',context)

def forgotPass(request):
    context={}
    return render(request,'users_app/user_authentication/userforgotPass.html',context)

def checkEmail(request):
    context={}
    return render(request,'users_app/user_authentication/userCheckEmail.html',context)

def logOut(request):
    logout(request)
    return redirect('register')

def newUserSignup(request):
    # if request.POST:
    #     form = MyUser(request.POST)
    #     print('Method==Post')
    #     if form.is_valid():
    #         form.save()
    #         return redirect(start)

    form = MyUser()
    if request.method == 'POST':
        print('we are here')
        form =MyUser(request.POST)
        print(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request,('Your profile was successfully updated!'))
            return redirect('users_app/user_authentication/userbuyVoucher.html')
        else:
            messages.error(request,('Please correct the error below.'))
            context={}
            return render(request, 'users_app/user_authentication/userBuysignup.html', context)
    else :
        form=MyUser(request.GET)
        form =MyUser()
        
    return render(request, 'users_app/user_authentication/userBuysignup.html',context={'form': form })

def LynBackupRegistration(request):

    if request.method == 'POST':
        # create a form that has request.POST
        form = UserCreationForm(request.POST)

        # check for the validity of the form
        if form.is_valid():

            #save username to flash success message
            username = form.cleaned_data.get('username') 

            # flash a success message for user
            messages.success(request, f'Account created for {username}')

            #redirect user to home page after sign up
            return redirect('start') #string provided in billing -> urls.py -> path for home

    else:
        form = UserCreationForm(request.POST)


    # render the page where form lives
    return render (request, 'users_app/user_authentication/register.html', {'form': form})
