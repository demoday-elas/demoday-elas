from django.shortcuts import render
from .models import Empresas, Usuaria
from app.forms import UsuariaForm, LoginForm

# from app.forms import UsuariaForm

# Create your views here.

def mostrar_index(request):
    return render(request, 'index.html')


def mostrar_cadastro(request):
    formulario = UsuariaForm(request.POST or None)
    msg = ''

    if formulario.is_valid():
        formulario.save()
        formulario = UsuariaForm()
        msg = 'Cadastro realizado com sucesso linda!!!!!!!'

    contexto = {
        'form': formulario,
        'msg':msg
    }
    return render (request, 'cadastro2.html', contexto)  

def mostrar_login(request):
    formulario = LoginForm(request.POST or None)
    msg = ''

    if formulario.is_valid():
        formulario.save()
        formulario = UsuariaForm()
        msg = 'Cadastro realizado com sucesso linda!!!!!!!'

    contexto = {
        'form': formulario,
        'msg':msg
    }
    return render (request, 'login3.html', contexto)

def mostrar_areas(request):
    return render (request, 'areas4.html')

def mostrar_vagas(request):    
    return render (request,'vagas5.html',)   

