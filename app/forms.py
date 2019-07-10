from django import forms
from app.models import Usuaria, Login, Empresas

class EmpresasForm(forms.ModelForm):
    class Meta:
        model = Empresas
        fields = [
            'nome',
            'endereco', 
            'cargo',
            'estado',
            'regiao', 
            'salario', 
            'qtd_vaga', 
            'Descricao_vaga',                                                                                                                                  
        ]

class UsuariaForm(forms.ModelForm):
    class Meta:
        model = Usuaria
        fields = [
            'usuaria',
            'senha',
            'nome',
            'sobrenome',
            'email', 
            'telefone',
            'nascimento',
        ]

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = [
            'nome',
            'sobrenome',
            'email',
            'senha',
        ]