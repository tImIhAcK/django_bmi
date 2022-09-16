from django.shortcuts import render, redirect
from .models import BMI
from .forms import BMIForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required()
def index(request):
    return render(request, 'bmi/index.html')

@login_required
def imperial(request):
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
    return render(request, 'bmi/imperial.html', context)

@login_required
def metric(request):
    form = BMIForm()
    if request.method == 'POST':
        form = BMIForm(request.POST)
        if form.is_valid():
            weight = request.POST.get('weight')
            height = request.POST.get('height')
            
            bmi = weight * height
                        # send to client side.
            return JsonResponse({"instance": bmi}, status=200)
            # obj = form.save()
            # messages.success(request, 'Saved....')
            # return redirect('bmi:index')
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)
    context = {
        'form': form,
    }
    return render(request, 'bmi/metric.html', context)