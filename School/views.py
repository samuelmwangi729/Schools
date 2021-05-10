from django.shortcuts import render,redirect
from  django.http import JsonResponse
from django.contrib import messages
from validate_email import validate_email
from .models import SuccessfulLogins
from django.contrib.auth.decorators import login_required
# Create your views here.
from  django.contrib.auth.models import User,auth
from .forms import SlidersForm
from . import models
def Index(request):
    return render(request,'Home.html',{'title':'HomePage'})
def About(request):
    return render(request,'About.html',{'title':'About Us'})
def Careers(request):
    return render(request,'Careers.html',{'title':'Careers'})
def News(request):
    return render(request,'News.html',{'title':'News Desk'})
def Contact(request):
    return render(request,'Contact.html',{'title':'Contact Us'})
@login_required
def Admin(request):
    return render(request,'Admin/Index.html',{'title':'Administrator Homepage| Management Console','name':'Dashboard'})
def Logout(request):
    auth.logout(request)
    return redirect('index')
def Login(request):
    if request.method=='POST':
        username=request.POST['Username']
        password=request.POST['password']
        #check if the email is valid
        if validate_email(username):
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                #if the user exists
                auth.login(request,user)
                x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
                if x_forwarded_for:
                    ip = x_forwarded_for.split(',')[0]
                else:
                    ip = request.META.get('REMOTE_ADDR')
                browser=request.META.get('HTTP_USER_AGENT')
                SuccessfulLogins.objects.create(username=username,browser=browser,ip=ip)
                if 'NextUrl' in request.session:
                    return redirect(request.session['NextUrl'])
                else:
                    return redirect('admin')
            else:
                messages.info(request,'Login Error,Either the password or the Email is Wrong')
                return redirect('login')
    else:
        if 'next' in request.GET:
            request.session['NextUrl']=request.GET.get('next')
        return render(request,'Login.html',{'title':'Portal Login'})
def Register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if password != password2:
            return redirect('registerform')
        else:
            if User.objects.filter(email=email).exists():
                messages.success(request,'user registration Not successful,Contact us for help')
                return redirect('register')
            else:
                user= User.objects.create_user(username=email,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                messages.success(request,'user registration successful,Kindly login to Access your Dashboard')
                return redirect('login')
    else:    
        return render(request,'Register.html',{'title':'Portal Registration'})
def Sliders(request):
    if request.method == 'POST':
        form=SlidersForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request,'Slider Successfully Added')
            return redirect('Sliders')
        else:
            messages.info(request,'Slider Could Not be  Added')
            return redirect('Sliders')
        pass
    else:
        form=SlidersForm()
        sliders=models.Sliders.objects.all()
        return render(request,'Admin/Sliders.html',{'title':'Manage Sliders','name':'Sliders','form':form,'sliders':sliders})