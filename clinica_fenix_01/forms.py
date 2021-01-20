from django import forms
from .models import Usuario
from django.core import validators


class IngresoUsuario(forms.Form):
    usuario = forms.CharField()
    clave = forms.CharField(widget=forms.PasswordInput)
 
class FormularioUsuario(forms.ModelForm):

    class Meta:
        model=Usuario
        fields='__all__'
    

