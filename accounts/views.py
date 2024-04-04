from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from accounts.forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
import re
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")
            if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', username):
                email = username
                user = User.objects.filter(email=email).first()
                if user:
                    username = user.username
                user = authenticate(request, username=username, password=password)
            else:
                user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.add_message(request, messages.INFO, "Login Failed! Please enter the username and password correctly.")
        
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('/')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form  = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        form = RegisterForm()
        context = {'form': form}
        return render(request, 'accounts/register.html', context)
    else:
        return redirect('/')

# Create your views here.
