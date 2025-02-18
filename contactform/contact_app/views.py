from django.shortcuts import render,redirect,get_object_or_404
from . models import Contact
from .forms import ContactForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User 

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

def list_contact(request):
    dict_insert = {
        'insert' : Contact.objects.all()
    }
    return render(request,'listContact.html',dict_insert)
    
    
def loginpage(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Changed from 'name' to 'email'
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)  # Get user by email
            user = authenticate(request, username=user.username, password=password)  # Authenticate using username
        except User.DoesNotExist:
            user = None

        if user is not None:
            if user.is_staff or user.is_superuser:  # Allow only staff or admin users
                auth_login(request, user)
                return redirect('list')
            else:
                messages.error(request, "Access restricted to admin only!")
                return redirect('login')
        else:
            messages.error(request, "Email or Password is incorrect!")
            return redirect('login')

    return render(request, "loginpage.html")


def views_page(request,id):
   coustomer = get_object_or_404(Contact, pk=id)  # Fetch student details
   return render(request, 'view.html', {'coustomer': coustomer})