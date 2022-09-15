from django.contrib import admin
from .models import BMI

@admin.register(BMI)
class BMIAdmin(admin.ModelAdmin):
    list_display = ['user', 'bmi', 'date']