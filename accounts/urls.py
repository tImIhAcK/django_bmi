from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.sign_in, name='login'),
    path('register/', views.sign_up, name='register'),
    path('logout/', views.log_out, name='logout')
]
