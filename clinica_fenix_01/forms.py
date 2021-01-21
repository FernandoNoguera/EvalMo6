from django import forms
from .models import Usuario, Examen
from django.core import validators


class IngresoUsuario(forms.Form):
    usuario = forms.CharField()
    clave = forms.CharField(widget=forms.PasswordInput)
 
class FormularioUsuario(forms.ModelForm):

    class Meta:
        model=Usuario
        fields='__all__'
    
 
class FormularioExamen(forms.ModelForm):

    class Meta:
        model=Examen
        fields='__all__'

