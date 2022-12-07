from django.http import HttpResponse
from django.shortcuts import render, redirect
from appcoder.models import *
from appcoder.forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from primer_proyecto.settings import BASE_DIR
import os


def index(request):
    if request.user.is_authenticated:
        if Avatar.objects.filter(user= request.user.id).order_by('-id'):
            imagen_model = Avatar.objects.filter(user= request.user.id).order_by('-id')[0]
            imagen_url = imagen_model.imagen.url
        else:
            imagen_url = ''
    else:
        imagen_url = ''
    return render(request, 'appcoder/index.html', {'imagen_url': imagen_url})

def Vista_Cursos(request):

    cursos = Curso.objects.all()
    
    return render(request, 'appcoder/cursos_vista.html', {'listado_cursos': cursos})


@login_required
def Cursos(request):

    return render(request, 'appcoder/cursos.html')


def Creacion_Curso(request):

    errores = ''

    if request.method == 'POST':
        formulario = Curso_Formulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            
            curso = Curso(nombre=data['nombre'], comision=data['comision'])

            curso.save()
        else:
            errores = formulario.errors

    formulario = Curso_Formulario()
    contexto = {'formulario': formulario, 'errores': errores}

    return render(request, 'appcoder/curso_formulario.html', contexto)


def Borrar_Curso(request, id):

    curso = Curso.objects.get(id=id)
    curso.delete()

    return redirect('cursos_vista')


def Editar_Curso(request, id):

    curso = Curso.objects.get(id=id)

    if request.method == 'POST':
        formulario = Curso_Formulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            curso.nombre = data['nombre']
            curso.comision = data['comision']
            curso.save()

            return redirect('cursos_vista')
        else:
            return render(request, 'appcoder/editar_curso.html', {'formulario': formulario, 'errores': formulario.errors})
    else:
        formulario = Curso_Formulario(initial={'nombre': curso.nombre, 'camada': curso.comision})
        return render(request, 'appcoder/editar_curso.html', {'formulario': formulario, 'errores': ''})

def Buscar_Curso(request):
    
    return render(request, 'appcoder/cursos.html')


def Resultado_Buscar_Curso(request):

    if request.GET['nombre_curso']:    
        nombre = request.GET['nombre_curso'] 
        curso = Curso.objects.filter(nombre__icontains = nombre)

        return render(request, 'appcoder/resultado_busqueda_cursos.html', {'curso': curso})

    else:
        rta = 'No enviaste datos!'
        return render(request, 'appcoder/resultado_busqueda_cursos.html', {'rta': rta})


def Vista_Estudiantes(request):
    
    estudiantes = Estudiante.objects.all()

    return render(request, 'appcoder/estudiantes_vista.html', {'listado_estudiantes': estudiantes})


def Estudiantes(request):

    return render(request, 'appcoder/estudiantes.html')

def Creacion_Estudiantes(request):
    
    errores = ''

    if request.method == 'POST':
        formulario = Estudiante_Formulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            
            estudiante = Estudiante(nombre=data['nombre'], apellido=data['apellido'], email=data['email'])

            estudiante.save()
        else:
            errores = formulario.errors

    formulario = Estudiante_Formulario()
    contexto = {'formulario': formulario, 'errores': errores}

    return render(request, 'appcoder/estudiantes_formulario.html', contexto)


def Borrar_Estudiante(request, id):

    estudiante = Estudiante.objects.get(id=id)
    estudiante.delete()

    return redirect('estudiantes_vista')


def Editar_Estudiante(request, id):

    estudiante = Estudiante.objects.get(id=id)

    if request.method == 'POST':
        formulario = Estudiante_Formulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            estudiante.nombre = data['nombre']
            estudiante.apellido = data['apellido']
            estudiante.email = data['email']
            estudiante.save()

            return redirect('estudiantes_vista')
        else:
            return render(request, 'appcoder/editar_estudiante.html', {'formulario': formulario, 'errores': formulario.errors})
    else:
        formulario = Estudiante_Formulario(initial={'nombre': estudiante.nombre, 'apellido': estudiante.apellido, 'email': estudiante.email})
        return render(request, 'appcoder/editar_estudiante.html', {'formulario': formulario, 'errores': ''})


def Buscar_Estudiante(request):
    return render(request, 'appcoder/estudiantes.html')


def Resultado_Buscar_Estudiante(request):

    if request.GET['nombre_estudiante']:    
        nombre = request.GET['nombre_estudiante'] 
        estudiante = Estudiante.objects.filter(nombre__icontains = nombre)

        return render(request, 'appcoder/resultado_busqueda_estudiante.html', {'estudiante': estudiante})

    else:
        rta = 'No enviaste datos!'
        return render(request, 'appcoder/resultado_busqueda_estudiante.html', {'rta': rta})


def Vista_Profesores(request):

    profesores = Profesor.objects.all()
    
    return render(request, 'appcoder/profesores_vista.html', {'listado_profesores': profesores})


def Profesores(request):

    return render(request, 'appcoder/profesores.html')    


def Creacion_Profesores(request):

    errores = ''

    if request.method == 'POST':
        formulario = Profesor_Formulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            
            profesor = Profesor(nombre=data['nombre'], apellido=data['apellido'], email=data['email'], profesion=data['profesion'])

            profesor.save()
        else:
            errores = formulario.errors

    formulario = Profesor_Formulario()
    contexto = {'formulario': formulario, 'errores': errores}

    return render(request, 'appcoder/profesores_formulario.html', contexto)
    

def Borrar_Profesor(request, id):

    profesor = Profesor.objects.get(id=id)
    profesor.delete()

    return redirect('profesores_vista')


def Editar_Profesor(request, id):


    if request.user.is_authenticated:

        profesor = Profesor.objects.get(id=id)

        if request.method == 'POST':
            formulario = Profesor_Formulario(request.POST)

            if formulario.is_valid():
                data = formulario.cleaned_data

                profesor.nombre = data['nombre']
                profesor.apellido = data['apellido']
                profesor.email = data['email']
                profesor.profesion = data['profesion']
                profesor.save()

                return redirect('profesores_vista')
            else:
                return render(request, 'appcoder/editar_profesor.html', {'formulario': formulario, 'errores': formulario.errors})
        else:
            formulario = Profesor_Formulario(initial={'nombre': profesor.nombre, 'apellido': profesor.apellido, 'email': profesor.email, 'profesion': profesor.profesion})
            return render(request, 'appcoder/editar_profesor.html', {'formulario': formulario, 'errores': ''})
    else:
        return redirect('auth_login')


def Buscar_Profesor(request):

    return render(request, 'appcoder/profesores.html')


def Resultado_Buscar_Profesor(request):

    if request.GET['nombre_profesor']:

        nombre = request.GET['nombre_profesor']
        profesor = Profesor.objects.filter(nombre__icontains = nombre)

        return render(request, 'appcoder/resultado_busqueda_profesor.html', {'profesor': profesor})

    else:
        rta = 'No enviaste datos!'
        return render(request, 'appcoder/resultado_busqueda_profesor.html', {'rta': rta})


class EntregablesList(LoginRequiredMixin, ListView):

    model = Entregable
    template_name = 'appcoder/list_entregables.html'


class EntregableDetail(DetailView):

    model = Entregable
    template_name = 'appcoder/detail_entregable.html'


class EntregableCreate(CreateView):

    model = Entregable
    success_url = '/coder/entregables/'
    fields = ['nombre', 'fecha_de_entrega', 'entregado']
    template_name = 'appcoder/entregable_form.html'

class EntregableUpdate(UpdateView):

    model = Entregable
    success_url = '/coder/entregables/'
    fields = ['fecha_de_entrega', 'entregado']

class EntregableDelete(DeleteView):

    model = Entregable
    success_url = '/coder/entregables/'


def Iniciar_Sesion(request):

    errors = ''
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            user = authenticate(username=data['username'], password=data['password'])

            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                return render(request, 'appcoder/login.html', {'form': formulario, 'errors': 'Credenciales Invalidas'})
        
        else:
            return render(request, 'appcoder/login.html', {'form': formulario, 'errors': formulario.errors})

    formulario = AuthenticationForm()
    return render(request, 'appcoder/login.html', {'form': formulario})


def Registrar_Usuario(request):

    if request.method == 'POST':
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
        else:
            return render(request, 'appcoder/register.html', {'form': formulario, 'errors': formulario.errors})

    formulario = UserRegisterForm()
    return render(request, 'appcoder/register.html', {'form': formulario})


@login_required
def Editar_Perfil(request):

    usuario = request.user

    if request.method == 'POST':
        formulario = UserEditForm(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario.email = data['email']
            usuario.first_name = data['first_name']
            usuario.last_name = data['last_name']

            usuario.save()
            return redirect('inicio')
        else:
            return render(request, 'appcoder/editar_perfil.html', {'form': formulario, 'errors': formulario.errors})
    
    else:
        formulario = UserEditForm(initial = {'email': usuario.email, 'first_name': usuario.first_name, 'last_name': usuario.last_name})
        
    return render(request, 'appcoder/editar_perfil.html', {'form': formulario})


@login_required
def Agregar_Avatar(request):
    
    if request.method == 'POST':
        formulario = AvatarForm(request.POST, files=request.FILES)
        print(request.FILES, request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario = request.user

            avatar = Avatar(user=usuario, imagen=data['imagen'])
            avatar.save()

            return redirect('inicio')
        else:
            return render(request, 'appcoder/agregar_avatar.html', {'form': formulario, 'errors': formulario.errors })
    formulario = AvatarForm()

    return render(request, 'appcoder/agregar_avatar.html', {'form': formulario})