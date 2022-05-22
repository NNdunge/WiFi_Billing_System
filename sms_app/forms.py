from django.forms import ModelForm
from .models import Sms_in

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError 


class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=20, label=False)
    email = forms.EmailField(max_length=100) 

    class Meta:
        model=User
        fields=['username','email','password1','password2']

    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.fields['username'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'True', 
            'name':'username', 
            'id':'username', 
            'type':'text', 
            'placeholder':'Username', 
            'maxlength': '25', 
            'minlength': '3', 
            }) 
        self.fields['email'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'True', 
            'name':'email', 
            'id':'email', 
            'type':'email', 
            'placeholder':'lnn@mail.com', 
            }) 
        self.fields['password1'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'True', 
            'name':'password1', 
            'id':'password1', 
            'type':'password', 
            'placeholder':'Password cant be entirely numeric', 
            'maxlength':'22',  
            'minlength':'5' 
            }) 
        self.fields['password2'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'True', 
            'name':'password2', 
            'id':'password2', 
            'type':'password', 
            'placeholder':'Confirm Password', 
            'maxlength':'22',  
            'minlength':'5' 
            }) 

    #Prevent to enter duplicate username.
    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return username  
  
    #Prevent to enter duplicate email.
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError(" Email Already Exist")  
        return email  

    #check both passwords are matched or not
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 != password2:  
            raise ValidationError("Password don't match")  
        return password2

    #save the data


       

   
