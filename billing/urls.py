"""billing URL Configuration

The `urlpatterns` list routes URLs to views.
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
from django.contrib import admin
from django.urls import path,include
from users_app import views as user_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(('landingpage.urls','landingpage'), namespace='start')),
    path('smsApp/' ,include(('sms_app.urls','sms_app'),namespace='myadmin')),
    path('userApp/',include(('users_app.urls','users_app'),namespace='users')),

    #backup path
    path (
        'registerbackup/', 
        user_views.LynBackupRegistration,
        name ='registerbackup'
    ),

]
