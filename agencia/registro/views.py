from django.shortcuts import render, redirect # type: ignore
from .models import *

from .forms import *

# Create your views here.
def home(request):
  return render(request, "registro/index.html")

def menu(request):
  return render(request, "registro/menu.html")

def habitacion(request):
  contexto = {"habitacion": Habitacion.objects.all()}
  return render(request, "registro/habitacion.html", contexto)

def hotel(request):
  contexto = {"hotel": Hotel.objects.all()}
  return render(request, "registro/hotel.html", contexto)

def pasajero(request):
  contexto = {"pasajero": Pasajero.objects.all()}
  return render(request, "registro/pasajero.html", contexto)

def pais_destino(request):
  contexto = {"pais_destino": Pais_destino.objects.all()}
  return render(request, "registro/pais_destino.html", contexto)

#___Formularios
def registro_form(request):
    if request.method == 'POST':
        form = registroForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('pasajero')  # Cambia '' por la URL a la que quieras redirigir
    else:
        form = registroForm()
    
    return render(request, "registro/registro_form.html", {"form": form})

def hotelform(request):
    if request.method == 'POST':
        form = hotelForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('hotel')  # Cambia '' por la URL a la que quieras redirigir
    else:
        form = hotelForm()
    
    return render(request, "registro/hotelform.html", {"form": form})

#_____Buscar
def buscarPasajeros(request):
    return render(request, "registro/buscar.html")

def encontrarPasajeros(request):
    if 'buscar' in request.GET:
        patron = request.GET.get('buscar')
        pasajeros = Pasajero.objects.filter(nombre__icontains=patron)
    else:
        pasajeros = Pasajero.objects.all()

    contexto = {'pasajero': pasajeros}
    return render(request, "registro/pasajero.html", contexto)