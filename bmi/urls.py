from django.urls import path
from . import views

app_name = 'bmi'
urlpatterns = [
    path('', views.index, name='index'),
    path('metric', views.metric, name='metric'),
    path('imperial', views.imperial, name='imperial')
]
