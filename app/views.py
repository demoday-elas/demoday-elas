from django.shortcuts import render
from .models import Empresas
# from app.forms import UsuariaForm

# Create your views here.

def mostrar_index(request):
    return render(request, 'index.html')


def mostrar_cadastro(request):
    # formulario = UsuariaForm (request.POST or None)
    # msg = ''

    # if formulario.is_valid():
    #     formulario.save()
    #     formulario = UsuariaForm()
    #     msg = 'Cadastro realizado com sucesso linda!!!!!!!'

    # contexto = {
    #     'form': formulario,
    #     'msg':msg
    # }
    return render (request, 'cadastro2.html',)  

def mostrar_login(request):
    return render (request, 'login3.html')

def mostrar_areas(request):
    return render (request, 'areas4.html')

def mostrar_vagas(request):
    
    empresa = Empresas.objects.all()
    return render (request,'vagas5.html', {'empresa': empresa})   

