# myproject/urls.py
from django.urls import path, include

urlpatterns = [
    path('', include('sectors.urls')),
]
