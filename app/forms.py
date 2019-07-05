from django import forms
from app.models import Empresas

class EmpresasForm(forms.ModelForm):
    class Meta:
        model = Empresas
        fields = [
            'empresa'
            'cargo'  
            'estado' 
            'regiao '
            'salario '
            'qtd_vaga '
            'Descricao_vaga'


from app.models import Usuaria

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