from django import forms
from .models import BMI
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class BMIForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'user',
            'weight', 
            'height',
            'bmi',
            Submit('submit', 'Calculate', css_class='col-md-6 justify-content-center')
        )
        
    def save(self, commit=True):
        bmi = super(BMIForm, self).save(commit=False)
        bmi.weight = self.cleaned_data.get('weight')
        bmi.height = self.changed_data.get('height')
        bmi.bmi = self.cleaned_data.get('bmi')
        if commit:
            bmi.save()
        return bmi
    
    
    class Meta:
        model = BMI
        fields = '__all__'
        
        
        