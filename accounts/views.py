from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        
        return render(request, 'accounts/login.html')
    else:
        return redirect('/')

def signin_view(request):
    return render(request, 'accounts/signin.html')

# Create your views here.
