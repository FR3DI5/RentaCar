from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.



def inicio(request):
    return HttpResponse("Bienvenido a RenataCar 🚗")


def inicio(request):
    return render(request, 'paginas/base.html')
