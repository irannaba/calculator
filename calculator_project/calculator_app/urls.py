from django.urls import path
from . import views

urlpatterns = [
    path('api/calculate/', views.calculate_exp, name='calculate'),
    path('api/history/', views.get_history, name='history'),
]
