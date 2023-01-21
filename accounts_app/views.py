from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login , logout, authenticate
from django.shortcuts import redirect
from .forms import UserCreateForm
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
# Create your views here.

def signupaccount(request):
    """ Sign up GET and POST request"""
    if request.method == 'GET':
        return render(request,'signup_account.html',{'form':UserCreateForm})
    else:
        print(request.POST['password1'])
        if request.POST['password1']==request.POST['password2']:
            try:
                user =User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('home')
            
            except IntegrityError:
                return render(request,'signup_account.html',{'form':UserCreateForm,'error':'Username already taken. Choose new username.'})
        else:
            return render(request,'signup_account.html',{'form':UserCreateForm,'error':'Passwords don\'t match'})

def loginaccount(request):
    """Login form craetion"""
    if request.method == 'GET':
        return render(request,'loginaccount.html',{'form': AuthenticationForm})

    else:
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'loginaccount.html',{'form': AuthenticationForm(),'error': 'username and password don\'t match'})

        else: 
            login(request,user)
            return redirect('home')  

@login_required
def logoutaccount(request):
    """Logout request"""
    logout(request)
    return redirect('home')