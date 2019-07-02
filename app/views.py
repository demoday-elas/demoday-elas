from django.shortcuts import render

# Create your views here.

def mostrar_index(request):
    return render(request, 'index.html')


def mostrar_cadastro(request):
    return render (request, 'cadastro2.html')  

def mostrar_login(request):
    return render (request, 'cadastro2.html')

def mostrar_areas(request):
    return render (request, 'areas4,html')

def mostrar_vagas(request):
    return render (request,'vagas5.html')   

