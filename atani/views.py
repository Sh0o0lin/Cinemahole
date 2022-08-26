import imp
from django.shortcuts import render
from .forms import LogInForm
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

def userLogin(request):
    if request.method=='POST':
        form=LogInForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('movie:CinemaHole'))
            else:
                messages.error(request,'Username or Password not correct')
                return HttpResponseRedirect(reverse('atani:login'))
    else:
        form=LogInForm()
    context={'form':form}
    return render(request,'atani/login.html',context)

def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('movie:CinemaHole'))