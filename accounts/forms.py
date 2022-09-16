from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'email',
            'password',
            Submit('submit', 'Register', css_class='col-md-6 justify-content-center')
        )
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'required': True}))
    email = forms.EmailField(required=True)
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'required': True}))
    class Meta:
        model = User
        fields = '__all__'
            
    def save(self, commit=True):
        user = super(LoginForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.password = self.cleaned_data['password']
        user.email = self.cleaned_data['email']
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
        fields = '__all__'