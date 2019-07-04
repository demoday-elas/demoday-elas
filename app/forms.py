
from django import forms
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
        ]