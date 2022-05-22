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
from sms_app import views

urlpatterns = [

    path('', csrf_exempt(views.register),name ='register'),
    path('smsIn/', views.smsInbox, name='smsin'),
    path('smsOut/', views.smsOutbox, name='smsout'),
    path('signin/', views.signIn,name='login'),
    path('logout/', views.logOut,name='logout'),
    path('voucher/', views.voucher,name='voucher'),
    path('register/', views.register,name='register'),
    path('forgot-password/', views.forgotPass, name='forgot-password'),
    path('check-email/', views.checkEmail),
    path('dashboard/', views.dashboard, name= 'home'),
]