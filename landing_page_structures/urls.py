from django.urls import path
from .views import landing_page, generate_data

urlpatterns = [
    path('', landing_page),
    path('generate_data', generate_data),
]
