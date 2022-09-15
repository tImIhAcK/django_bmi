from django import forms
from .models import BMI
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class BMIForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'weight', 
            'height',
            Submit('submit', 'Calculate', css_class='col-md-6 justify-content-center')
        )
    class Meta:
        model = BMI
        fields = '__all__'
        
        
        