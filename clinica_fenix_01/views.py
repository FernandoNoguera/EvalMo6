from django.shortcuts import render, redirect 
from django.conf import settings
from .forms import IngresoUsuario, FormularioUsuario
import json
from .models import Usuario
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View

def inicio(request):  
    return render(request, 'clinica_fenix_01/index.html')

def login(request):
    formulario = IngresoUsuario(request.POST or None)
    context = {'form':formulario}
    if formulario.is_valid():
        form_data = formulario.cleaned_data
        filename = "/clinica_fenix_01/static/clinica_fenix_01/data/usuario.json"
        with open(str(settings.BASE_DIR)+filename, 'r') as file:
            usuario=json.load(file)
        if (form_data['usuario'] == usuario['usuario']) and (form_data['clave'] == usuario['clave']):
            return redirect('clinica_fenix_01:portal_privado')               
        else:
            return redirect('clinica_fenix_01:login')               
    return render(request, 'clinica_fenix_01/registro.html',context)

def private_page(request):
    listaedad = []
    listapellido = []
    filename= "/clinica_fenix_01/static/clinica_fenix_01/data/clientes.json"
    with open(str(settings.BASE_DIR)+filename, "r") as file:
        usuarios = json.load(file)
        diccionario = usuarios.get('usuario')
        for elemento in diccionario:
            edad = elemento.get('edad')
            edad = int(edad)
            listaedad.append(edad)
        for elemento in diccionario:
            apellido = elemento.get('apellido_paterno')
            listapellido.append(apellido)
    context = {'edades' : listaedad, 'apellidos': listapellido}
    return render(request, 'clinica_fenix_01/PagePrivate.html', context)

def nuevo_usuario(request):
    formulario = NewUser(request.POST or None)
    context = {'form':formulario}
    if formulario.is_valid():
        form_data = formulario.cleaned_data
        filename= "/clinica_fenix_01/static/clinica_fenix_01/data/clientes.json"
        with open(str(settings.BASE_DIR)+filename, 'r') as file:
            usuario=json.load(file)
        form_data['id'] = usuario['ultimo_id_generado'] + 1
        usuario['ultimo_id_generado'] = form_data['id']
        usuario['usuario'].append(form_data)
        with open(str(settings.BASE_DIR)+filename, 'w') as file:
            json.dump(usuario, file)
        return redirect('clinica_fenix_01:lista_usuario')               
    return render(request, 'clinica_fenix_01/new_user.html', context)

def usuarios_registrados(request):
    filename= "/clinica_fenix_01/static/clinica_fenix_01/data/clientes.json"
    with open(str(settings.BASE_DIR)+filename, 'r') as file:
        clientes=json.load(file)
    return render(request, 'clinica_fenix_01/lista_usuario.html', context=clientes)

def eliminar_cliente(request, id):
    if request.method == "POST":
        filename= "/clinica_fenix_01/static/clinica_fenix_01/data/clientes.json"
        with open(str(settings.BASE_DIR)+filename, 'r') as file:
            clientes=json.load(file)
        for cliente in clientes['usuario']:
            if int(cliente['id']) == int(id):
                clientes['usuario'].remove(cliente)
                break
        with open(str(settings.BASE_DIR)+filename, 'w') as file:
            json.dump(clientes, file)
        return redirect('clinica_fenix_01:lista_usuario')
    context = {'id':id}
    return render(request, 'clinica_fenix_01/eliminar_cliente.html', context)

def render_cliente(request, id):
    filename= "/clinica_fenix_01/static/clinica_fenix_01/data/clientes.json"
    with open(str(settings.BASE_DIR)+filename, 'r') as file:
        clientes=json.load(file)
    for cliente in clientes['usuario']:
        if int(cliente['id']) == int(id):
            cliente_datos = cliente
    context = {'id':id, 'cliente': cliente_datos }
    return render(request, 'clinica_fenix_01/render_cliente.html', context)


class ListaPacientes(ListView):
    model= Usuario
    template_name= "clinica_fenix_01/lista_usuario.html"
    #context_object_name = ""}
    #extra_context = {''}




class CrearUsuario(CreateView):
    model = Usuario
    fields = '__all__'
    success_url = reverse_lazy('clinica_fenix_01:lista_usuario')


class EliminarPaciente(DeleteView):
    model = Usuario
    fields = '__all__'
    success_url = reverse_lazy('clinica_fenix_01:lista_usuario')


class EditarPaciente(UpdateView):
    model = Usuario
    fields = '__all__'
    success_url = reverse_lazy('clinica_fenix_01:lista_usuario')

    

