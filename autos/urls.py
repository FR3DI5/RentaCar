from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('autos/', views.autos, name='autos'),
    path('contacto/', views.autos, name='contacto'),
]


