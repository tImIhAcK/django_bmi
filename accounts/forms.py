from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username', 
            'password',
            Submit('submit', 'Login', css_class='col-md-6 justify-content-center')
        )
    class Meta:
        model = User
        fields = '__all__'
        
class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'email',
            'password',
            Submit('submit', 'Register', css_class='col-md-6 justify-content-center')
        )
    class Meta:
        model = User
        fields = '__all__'