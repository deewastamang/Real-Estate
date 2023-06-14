from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from contacts.models import Contact
# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are Now Logged in")
            return redirect('dashboard')
        else:
            messages.error(request, "Username not Valid")
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "You Have been Logged out Successfully !!")
    return redirect('index')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                # error message
                messages.error(request, "Username Already Exists")
                return render(request, 'accounts/register.html')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email Already Exists")
                    return render(request, 'accounts/register.html')
                else:
                    user = User.objects.create_user(username=username, password=password2, email=email, first_name=fname, last_name=lname)
                    # login after register
                    user.save()
                    messages.success(request, "Account Register Successfully")
                    return redirect('login')

        else:
            messages.error(request, "Password Did't Match")
            return render(request, 'accounts/register.html')
    else:
        return render(request, 'accounts/register.html')


def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    contaxt = {
        'contacts': user_contacts
    }

    return render(request, 'accounts/dashboard.html', contaxt)
