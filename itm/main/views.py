from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from .models import Contacts
# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                Contacts.objects.create(**form.cleaned_data)

                return redirect('contact')
            
            except:
                form.add_error(None, "Daten wurden nicht gesendet")

    else:
        form = ContactForm()
    
    context = {'form': form}
    return render(request, 'main/contact.html', context=context )



def impressum(request):
    return render(request, 'main/impressum.html')


def privacy(request):
    return render(request, 'main/privacy.html')