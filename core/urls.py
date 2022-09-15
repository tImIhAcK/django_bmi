from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('bmi.urls', namespace='bmi')),
    path('accounts/', include('accounts.urls', namespace='accounts'))
] + staticfiles_urlpatterns()