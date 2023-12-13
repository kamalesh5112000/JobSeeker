from django.shortcuts import render

def users(request):
    context={}
    return render(request,"users/userLogin.html",context)

def userSignup(request):
    context={}
    return render(request,"users/userSignup.html",context)

# Create your views here.
