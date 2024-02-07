from django.shortcuts import render

def home_page(request):
    return render(request, 'website/index.html')

def about_page(request):
    return render(request, 'website/about.html')

def elements_page(request):
    return render(request, 'website/elements.html')

def contact_page(request):
    return render(request, 'website/contact.html')


# Create your views here.
