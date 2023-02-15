from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def registration(request):
    return render(request,'registration/registrationSchoolSite.html')
# Create your views here.
