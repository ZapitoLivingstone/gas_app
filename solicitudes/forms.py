from django import forms
from .models import Solicitud

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['rut', 'nombre', 'apellido', 'direccion', 'telefono', 'comuna']