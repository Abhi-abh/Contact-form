from django.shortcuts import render,redirect
from . models import Contact
from .forms import ContactForm
from django.contrib import messages

# Create your views here.

def contact(request):
    form = ContactForm()  

    if request.method == "POST":
        form = ContactForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form Successfully Submitted')
            return redirect('contact')
    return render(request, "contact.html", {"form": form})
