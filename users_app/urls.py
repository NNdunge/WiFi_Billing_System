"""The `urlpatterns` list routes URLs to views
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from . import views

urlpatterns = [

    #path('register/', views.register,name='register'),
    path('signIn/', views.signIn,name='signin'),
    path('forgot-password/', views.forgotPass, name='forgot-password'),
    path('check-email/', views.checkEmail, name='checkemail'),
    # path('', views.newUserSignup, name= 'buyRegistration'),  

    #back up
    path('userRegister/', views.LynBackupRegistration, name= 'userRegistration'),
]