from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.hashers import make_password

# User = get_user_model()

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'email',
            'password1',
            'password2',
            Submit('submit', 'Register', css_class='col-md-6 justify-content-center')
        )
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'required': True}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'required':True}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'required': True}))
    password2 = forms.CharField(label='Confirm password',widget=forms.PasswordInput(attrs={'required': True}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
            
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.username = self.cleaned_data.get('username')
        user.set_password(make_password(self.cleaned_data.get('password1')))
        user.email = self.cleaned_data.get('email')
        user.is_active = True
        if commit:
            user.save()
        return user
        
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'password',
            Submit('submit', 'Login', css_class='col-md-6 justify-content-center')
        )
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'required': True}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'required': True}))
    class Meta:
        model = User
        fields = ('username', 'password')