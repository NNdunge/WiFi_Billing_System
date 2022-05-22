from django.urls import path
from landingpage import views

urlpatterns = [

    path('', views.mypage, name='mainpage'),
]