from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from .models import User

# Create your views here.
from Test import models
#初步完成登录
def login(request):
    if request.method =='POST':
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'login.html',{'error':'username wrong'})
        else:
            login(request,user)
            return redirect('index.html')

    else:
        return render(request,'index.html')  #
#注册接口
def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            login(request, user)
            return redirect('index.html')
    else:
        form = UserCreationForm()
    content = {'register':form}
    return render(request, 'register.html',content)



def index(request):
    return render(request, 'shouye.html')


