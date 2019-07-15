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
        labels = {
            "usuaria": "Usuária",
            "email": "E-mail"
        }


class LoginForm(forms.Form):
    usuario = forms.CharField(label='Usuária')
    senha = forms.CharField(label= 'Senha', widget=forms.PasswordInput())        