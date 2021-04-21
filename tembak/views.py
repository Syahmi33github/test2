from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

from django.contrib.auth import authenticate, login as dji_login, logout as dji_logout
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
from .forms import CreateUserForm

def index(request):
    context = {
        'Judul' : 'ATTA',
        'Content' : 'Silahkan Log in',
    }

    if request.method == "POST":
        username_login = request.POST['username']
        password_login = request.POST['password']
        user = authenticate(request, username=username_login, password=password_login)
        
        if user is not None:
            dji_login(request,user)
            return redirect('isi')
        else:
            messages.error(request, "Username/Password Tidak Cocok Coba Lagi")
    return render(request, 'index.html', context)

def isi(request):
    context = {
        'Judul' : 'ATTA',
        'Content' : 'Silahkan Log in',
    }

    return render(request, 'isi.html', context)