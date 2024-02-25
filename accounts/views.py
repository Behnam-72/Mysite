from django.shortcuts import render

def login_view(request):
    return render(request, 'accounts/login.html')

#def logout_view(request):
#    return render(request, 'accounts/logout.html')

def signin_view(request):
    return render(request, 'accounts/signin.html')

# Create your views here.
