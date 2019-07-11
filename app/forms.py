from django import forms
from app.models import Usuaria, Empresas

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


class LoginForm(forms.Form):
    usuario = forms.CharField(label='Usuario')
    senha = forms.CharField(label= 'Senha', widget=forms.PasswordInput())        