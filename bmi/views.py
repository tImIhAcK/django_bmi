from django.shortcuts import render, redirect
from .models import BMI
from .forms import BMIForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect

@login_required
def index(request):
    form = BMIForm()
    if request.method == 'POST':
        weight_metric = request.POST.get('weight')
        weight_imperial = request.POST.get('weight-imperial')
        
        bmi_result = bmi(request, metric=weight_metric, imperial=weight_imperial)
        
        print(bmi_result)
        # form = BMIForm(request.POST)
        # if form.is_valid():
        #     user = request.user.id
        #     weight = request.POST.get('weight')
        #     height = request.POST.get('height')
            
        #     bmi = (weight / (height**2))
        #                 # send to client side.
        #     return JsonResponse({"instance": bmi}, status=200)
        #     # obj = form.save()
        #     # messages.success(request, 'Saved....')
        #     # return redirect('bmi:index')
    context = {
        'form': form,
    }
    return render(request, 'bmi/index.html', context)


def bmi(request, metric=None, imperial=None):
    if metric:
        weight = float(request.POST.get('weight'))
        height = float(request.POST.get('height'))
    elif imperial:
        weight = float(request.POST.get('weight-imperial'))/2.205
        height = (float(request.POST.get('feets'))*30.34 + float(request.POST.get('feets'))*2.54)/100
        
    bmi_result = (weight/(height)**2)
    return bmi_result