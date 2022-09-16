from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm
from django.contrib import messages


def sign_in(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login succesfully')
                return redirect('bmi:index')
            else:
                messages.warning(request, 'User does not exist... Create an acount')
        else:
            messages.error(request, 'Invalid username or password')
            
    form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully.')
            return redirect('bmi:index')
        messages.warning(request, 'Invalid credentials')
    form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def log_out(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('/')
        
    