from django.shortcuts import render, HttpResponseRedirect
from website.forms import ContactForm, NewsletterForm
from django.contrib import messages

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
            new_name = form.save()
            new_name.name = 'Unknown'
            new_name.save()
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your message submitted successfully')
        else:
            messages.add_message(request, messages.ERROR, 'Your message didnt submit')
    form = ContactForm() 
    return render(request, 'website/contact.html', {'form': form})

def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')

# Create your views here.
