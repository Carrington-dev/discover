from django.shortcuts import redirect, render
from django.contrib import messages
from contact.forms import ContactForm

def home(request):
    context = dict()
    # context['title'] = "About"
    return render(request, 'basic/home.html', context)

def about(request):
    context = dict()
    context['title'] = "About"
    return render(request, 'basic/about.html', context)

def portfolio(request):
    context = dict()
    context['title'] = "Portfolio"
    return render(request, 'basic/portfolio.html', context)

def services(request):
    context = dict()
    context['title'] = "Services"
    return render(request, 'basic/services.html', context)

def contact(request):
    context = dict()
    context['title'] = "Contact"
    
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f"Your message has been sent. Thank you!")
            return redirect('home')

    else:
        context['form'] = form
    return render(request, 'basic/contact.html', context)

