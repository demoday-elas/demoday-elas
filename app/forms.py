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
        ]