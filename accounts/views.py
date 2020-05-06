from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def login(request):
    if request.method=='POST':
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return render(request,'accounts/ho.html')

        else:
            return render(request,'accounts/login.html',{'error':'invalid username or password'})
    else:

        return render(request,'accounts/login.html')


def signup(request):
    if request.method=='POST':
        if request.POST['password1']==request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request,'accounts/signup.html',{'error':'username has already been taken'})
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['username'],last_name=request.POST['lname'],email=request.POST['email'],first_name=request.POST['fname'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('homes')
        else:
            return render(request,'accounts/signup.html',{'error':'passwords must match'})
    else:


        return render(request,'accounts/signup.html')


def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('homes')
    return render(request,'accounts/signup.html')
