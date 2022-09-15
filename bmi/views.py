from django.shortcuts import render, redirect
from .models import BMI
from .forms import BMIForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required()
def index(request):
    form = BMIForm()
    if request.method == 'POST':
        form = BMIForm(request.POST)
        if form.is_valid():
            obj = form.save()
            messages.success(request, 'Saved....')
            return redirect('bmi:index')
    context = {
        'form': form,
    }
    return render(request, 'bmi/index.html', context)