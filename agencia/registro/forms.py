from django import forms # type: ignore
from .models import Pasajero, Hotel

class registroForm(forms.ModelForm):
    class Meta:
        model =  Pasajero   # type: ignore
        fields = ['nombre', 'apellido', 'email', 'sexo']

class hotelForm(forms.ModelForm):
    class Meta:
        model =  Hotel   # type: ignore
        fields = ['nombre','CheckIn', 'CheckOut', 'numeroNoches']
        widgets = {
            'CheckIn': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'CheckOut': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }