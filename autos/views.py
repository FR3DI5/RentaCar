from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.



def inicio(request):
    return HttpResponse("Bienvenido a RentaCar 🚗")


def inicio(request):
    return render(request, 'paginas/base.html')

def about(request):
    return render(request, 'paginas/about.html')

def login(request):
    return render(request, 'paginas/login.html')

def autos(request):
    return render(request, 'paginas/autos.html')

def contacto(request):
    return render(request, 'paginas/contacto.html')