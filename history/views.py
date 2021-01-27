from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

from django.contrib.auth import authenticate, login as dji_login, logout as dji_logout
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
from .forms import CreateUserForm

def index(request):
    context = {
        'judul' : 'HISTORY',
        'judulHalaman' : 'Home Form!!!',
    }
    return render(request, 'index.html', context)

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            # messages.success(request, 'Akun ' + user + ' berhasil dibuat')

            return redirect ('login')
        else :
            print('ihiy')   

    context = {
        'form' : form,
        'Judul' : 'Register!!!',
        'Content' : 'Silahkan registrasi',
    }
    return render(request, 'register.html', context)

def login(request):
    context = {
        'Judul' : 'LOG IN',
        'Content' : 'Silahkan Log in',
    }

    if request.method == "POST":
        username_login = request.POST['username']
        password_login = request.POST['password']
        user = authenticate(request, username=username_login, password=password_login)
        
        if user is not None:
            dji_login(request,user)
            return redirect('blog:listpage', page='1')
        else:
            messages.error(request, "Username/Password Tidak Cocok Coba Lagi")
        
    return render(request, 'login.html', context)
