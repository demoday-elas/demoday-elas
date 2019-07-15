from django.db import models

# Create your models here.

estado_opc = [
    ('AC', 'Acre'), 
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MG', 'Minas Gerais'),
    ('MS', 'Mato Grosso do Sul'),
    ('MT', 'Mato Grosso'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('PR', 'Paraná'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('RS', 'Rio Grande do Sul'),
    ('SC', 'Santa Catarina'),
    ('SE', 'Sergipe'),
    ('SP', 'São Paulo'),
    ('TO', 'Tocantins')
]

class Empresas(models.Model):
    nome = models.CharField(max_length=100, default='')
    endereco = models.CharField (max_length=100, default='')
    cargo  = models.CharField(max_length=100, default='')
    estado = models.CharField(max_length=2, choices=estado_opc, default='')
    salario = models.CharField(max_length=50, default='')
    qtd_vaga = models.DecimalField(max_digits=8, decimal_places=0)
    Descricao_vaga = models.TextField()
    
    def __str__(self):
        return self.nome


class Usuaria(models.Model):
    usuaria = models.CharField(max_length=20, default='')
    senha = models.CharField(max_length=20, default='')
    nome = models.CharField(max_length=50, default='')
    sobrenome = models.CharField(max_length=50, default='')
    email = models.EmailField()
    telefone = models.CharField(max_length=14, default='')
    nascimento = models.DateField()

    def __str__(self):
        return self.usuaria

   


