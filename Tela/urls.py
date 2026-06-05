from django.urls import path
from app_tela import views

urlpatterns = [
    path('', views.home, name='home'),
]