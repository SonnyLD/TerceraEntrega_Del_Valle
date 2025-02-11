from django.db import models # type: ignore

# Create your models here.
class Pais_destino(models.Model):
  nombre = models.CharField(max_length=50)
  fechaLLegada=models.DateTimeField()
  
  def __str__(self):
    return f"{self.nombre}"
  
  
class Hotel(models.Model):
  nombre = models.CharField(max_length=50)
  CheckIn=models.DateTimeField()
  CheckOut=models.DateTimeField()
  numeroNoches = models.IntegerField(default=1)
  
  def __str__(self):
    return f"{self.nombre}"


class Habitacion(models.Model):
  numero = models.IntegerField()
  doble = models.CharField(max_length=40)
  simple = models.CharField(max_length=40)

  def __str__(self):
    return f"{self.nombre}"
  
class Pasajero(models.Model):
  nombre = models.CharField(max_length=50)
  apellido = models.CharField(max_length=50)
  email = models.EmailField() 
  sexo = models.CharField(max_length=50) 

  class Meta:

    verbose_name = "Pasajero"
    verbose_name_plural = "Pasajeros"

  def __str__(self):
    return f"{self.nombre}"
  


   

