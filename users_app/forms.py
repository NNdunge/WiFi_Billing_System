from users_app.models import UserSignup,VoucherRequest
from django.forms import ModelForm
from django.core.exceptions import ValidationError


class MyUser(ModelForm):
    class Meta:
        model=UserSignup
        fields=['firstName','lastName','dob','gender','email','location']

    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.fields['firstName'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'firstName', 
            'id':'firstName', 
            'type':'text', 
            'placeholder':'FirstName', 
            'maxlength': '16', 
            'minlength': '3', 
            }) 
        self.fields['lastName'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'lastName', 
            'id':'lastName', 
            'type':'text', 
            'placeholder':'lastName', 
            'maxlength': '16', 
            'minlength': '3', 
            }) 
        self.fields['dob'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'dob', 
            'id':'dob', 
            'type':'date', 
            'placeholder':'dob', 
            }) 
        self.fields['gender'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'gender', 
            'id':'gender', 
            'type':'text', 
            'placeholder':'gender', 
            }) 
        self.fields['email'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'email', 
            'id':'email', 
            'type':'email', 
            'placeholder':'lyn@gmail.com',  
            }) 
        self.fields['location'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'location', 
            'id':'location', 
            'type':'text', 
            'placeholder':'location', 
            })
    def firstname_clean(self):  
        firstName = self.cleaned_data['firstName'].lower()  
        new = MyUser.objects.filter(firstName = firstName)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return firstName 
    def lastname_clean(self):  
        LastName = self.cleaned_data['LastName'].lower()  
        new = MyUser.objects.filter(LastName= LastName)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return LastName  
  
    #Prevent to enter duplicate email.
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = MyUser.objects.filter(email=email)  
        if new.count():  
            raise ValidationError(" Email Already Exist")  
        return email  
        
