from django.shortcuts import render

# Create your views here.
def mypage(request):
    context={}
    return render(request,'landingpage/mainpage.html',context)
   