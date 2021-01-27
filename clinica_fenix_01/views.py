from django.shortcuts import render, redirect 
from django.conf import settings
from .forms import IngresoUsuario, FormularioUsuario, ContactForm
import json
from .models import Usuario, Examen, Profile
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View
import requests
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.conf import settings
import random
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views import generic


def inicio(request):
    formulario = ContactForm(request.POST or None)
    context = {'form':formulario}
    if request.method == "POST":
        formulario = ContactForm(request.POST)
        if formulario.is_valid():
            infoform = formulario.cleaned_data
            filename = "\clinica_fenix_01\static\clinica_fenix_01\data\contactos.json"
            with open(str(settings.BASE_DIR)+filename, "r") as file:
                usuario = json.load(file)
            infoform['id'] = usuario['ultimo_id_generado'] + 1
            usuario['ultimo_id_generado'] = infoform['id']
            usuario['usuario'].append(infoform)
            with open(str(settings.BASE_DIR)+filename, 'w') as file:
                json.dump(usuario, file)
            asunto = infoform['asunto']
            nombre = infoform['name']
            emailcontacto = infoform['email']
            message = infoform['message']
            respuesta = ['Hola ', nombre,'. \n Hemos recibido tu mensaje:\n \n',
                        message, '\n \n Pronto nuestro equipo se pondrá en contacto con usted al correo indicado: \n \n',
                        emailcontacto, '\n \n Saludos del equipo. \n Clinica Fenix S.A.']
            respuesta = "".join(map(str, respuesta))   
            email = EmailMessage(asunto, respuesta, to=[emailcontacto])
            emaily = EmailMessage('Correo de Prueba desde Django', 'Enviando correo de prueba', to=['Fnoguerav25@gmail.com'])  
            email.send()
            return redirect('clinica_fenix_01:index')     
    return render(request, 'clinica_fenix_01/index.html',context)

# se comenta por nuevo login def login(request):
# se comenta por nuevo login     formulario = IngresoUsuario(request.POST or None)
# se comenta por nuevo login     context = {'form':formulario}
# se comenta por nuevo login     if formulario.is_valid():
# se comenta por nuevo login         form_data = formulario.cleaned_data
# se comenta por nuevo login         filename = "/clinica_fenix_01/static/clinica_fenix_01/data/usuario.json"
# se comenta por nuevo login         with open(str(settings.BASE_DIR)+filename, 'r') as file:
# se comenta por nuevo login             usuario=json.load(file)
# se comenta por nuevo login         if (form_data['usuario'] == usuario['usuario']) and (form_data['clave'] == usuario['clave']):
# se comenta por nuevo login             return redirect('clinica_fenix_01:portal_privado')               
# se comenta por nuevo login         else:
# se comenta por nuevo login             return redirect('clinica_fenix_01:login')               
# se comenta por nuevo login     return render(request, 'clinica_fenix_01/registro.html',context)

@login_required(login_url='/accounts/login/')
def private_page(request):
    dic1 = {}
    dic2 = {}
    edad = []
    apellidos = []
    usuarios = Usuario.objects.all().values()
    for i in usuarios:
        for key,value in i.items():
            dic1 = key,value
            if key == 'edad':
                edad.append(value)
            elif key == 'apellido_paterno':
                apellidos.append(value)
            else:
                continue
    context = {'edad': edad, 'nombre':apellidos , 'usuarios': usuarios}
    return render(request, 'clinica_fenix_01/PagePrivate.html', context)


class ListaPacientes(ListView):
    model= Usuario
    template_name= "clinica_fenix_01/lista_usuario.html"
    context_object_name = "Usuario"
    #extra_context = {'usuario': usuarios }



class CrearUsuario(CreateView):
    model = Usuario
    template_name= "clinica_fenix_01/new_user.html"
    fields = '__all__'
    success_url = reverse_lazy('clinica_fenix_01:lista_usuario')


class EliminarPaciente(DeleteView):
    model = Usuario
    template_name= "clinica_fenix_01/eliminar_cliente.html"
    context_object_name = "Usuario"
    fields = '__all__'
    success_url = reverse_lazy('clinica_fenix_01:lista_usuario')


class EditarPaciente(UpdateView):
    model = Usuario
    template_name= "clinica_fenix_01/editar_cliente.html"
    fields = '__all__'
    success_url = reverse_lazy('clinica_fenix_01:lista_usuario')

    
class ListaExamenes(ListView):
    model= Examen
    template_name= "clinica_fenix_01/lista_examen.html"
    context_object_name = "Examenes"
    #extra_context = {''}


class CrearExamen(CreateView):
    model = Examen
    template_name= "clinica_fenix_01/new_examen.html"
    fields = '__all__'
    success_url = reverse_lazy('clinica_fenix_01:lista_examen')


class EliminarExamen(DeleteView):
    model = Examen
    template_name= "clinica_fenix_01/eliminar_examen.html"
    context_object_name = "Examenes"
    fields = '__all__'
    success_url = reverse_lazy('clinica_fenix_01:lista_examen')


class EditarExamen(UpdateView):
    model = Examen
    template_name= "clinica_fenix_01/editar_examen.html"
    fields = '__all__'
    success_url = reverse_lazy('clinica_fenix_01:lista_examen')

def examen_cliente(request, pk):
    dic1 = {}
    data_num = []
    usuarios = Usuario.objects.all().values()
    examen = Examen.objects.all().values()
    for cliente in usuarios:
        if int(cliente['id']) == int(pk):
            cliente_datos = cliente
    #### dato 1 Plaquetas
    for cliente in examen:
        if int(cliente['usuario_id_id']) == int(pk):
            for key,value in cliente.items():
                dic1 = key,value
                if key == 'plaquetas':
                    data_num.append(value)
                elif key == 'globulos_blancos':#### dato 2 G blancos
                    data_num.append(value)
                elif key == 'globulos_rojos':##### dato 3 G rojos
                    data_num.append(value)
                elif key == 'hematocritos': ##### dato 4 Hematocrito
                    data_num.append(value)
                else:
                    continue
        else:
            pass
    context = {'id':id, 'cliente': cliente_datos, 'data_num': data_num , 'examen': examen }
    return render(request, 'clinica_fenix_01/render_cliente.html', context)


class Registro(generic.CreateView):
    form_class = UserCreationForm
    template_name= "clinica_fenix_01/registro.html"
    #extra_context = {'formulario'}
    success_url = reverse_lazy('clinica_fenix_01:login')

