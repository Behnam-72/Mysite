from django.shortcuts import render, HttpResponse
from website.forms import ContactForm
def home_page(request):
    return render(request, 'website/index.html')

def about_page(request):
    return render(request, 'website/about.html')

def elements_page(request):
    return render(request, 'website/elements.html')

def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm() 
    return render(request, 'website/contact.html', {'form': form})


# Create your views here.
