from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm
from django.contrib import messages


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        form = LoginForm(data=request.POST)
        # form = form.cleaned_data
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login succesfully')
            else:
                messages.error(request, 'User does not exist... Create an acount')
                return render(request, 'accounts/auths.html', {'form': form})
    return render(request, 'accounts/auths.html', {'form': form})

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Account created successfully')
        else:
            messages.error(request, 'Invalid')
            return render(request, 'accounts/auths.html', {'form': form})
    return render(request, 'accounts/auths.html', {'form': form})

def logout(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('/')
        
    