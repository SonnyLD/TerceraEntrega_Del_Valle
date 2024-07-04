from django.urls import path, include # type: ignore
from registro.views import *

urlpatterns = [
    path('', home, name = "home"),
    path('menu/', menu, name = "menu"),
    path('habitacion/', habitacion, name = "habitacion"),
    path('hotel/', hotel, name = "hotel"),
    path('pasajero/', pasajero, name = "pasajero"),
    path('pais_destino/', pais_destino, name = "pais_destino"),

    #___formularios__

    path('registro_form/', registro_form, name="registro_form"),
    path('hotelform/', hotelform, name="hotelform"),

    path('buscarPasajeros/', buscarPasajeros, name="buscarPasajeros"),
    path('encontrarPasajeros/', encontrarPasajeros, name="encontrarPasajeros"),
]
