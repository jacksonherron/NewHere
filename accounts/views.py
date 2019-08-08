from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = email
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                return render(request, 'register.html', {'error': 'That email is already connected to an account. Please Log in.'})
            else:
                user = User.objects.create_user(
                    first_name = first_name,
                    last_name = last_name,
                    email = email,
                    username = username, 
                    password = password,
                    )
                user.save()
                return redirect('login')
        else:
            return render(request, 'register.html', {'error': 'Passwords do not match'})
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid Credentials'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('landing_page.html')