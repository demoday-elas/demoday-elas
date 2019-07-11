from django.shortcuts import render, redirect
from app.models import Usuaria
from app.models import Empresas
from app.forms import UsuariaForm, LoginForm, EmpresasForm

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
        msg = 'Cadastro realizado com sucesso, vamos para o próximo passo? -->!!'

    contexto = {
        'form': formulario,
        'msg':msg   
    } 

    return render (request, 'cadastro2.html', contexto)  

def mostrar_login(request):
    formulario_login = LoginForm(request.POST or None) 
    msg = ' '
    if formulario_login.is_valid():
        usuario = formulario_login.cleaned_data['usuario']
        senha = formulario_login.cleaned_data['senha']
        user = Usuaria.objects.filter(usuaria=usuario).first()
        
        if not user or user.senha != senha:
            msg = 'Verifique novamente'
        else:
            return redirect('/areas')

    return  render(request, 'login3.html', {'form': formulario_login, 'msg': msg})

def mostrar_areas(request):
    vagas = Usuaria.objects.all()
    return render (request, 'areas4.html', {'vagas':vagas})

def mostrar_vagas(request):  
    vaga = Empresas.objects.all()  
    return render (request,'vagas5.html', {'vaga':vaga})   

