# sectors/urls.py
from django.urls import path
from .views import SectorCoursesView

urlpatterns = [
    path('api/sectors/<str:sector_name>/', SectorCoursesView.as_view(), name='sector-courses'),
]
