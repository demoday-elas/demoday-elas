from django.db import models

# Create your models here.

zonas = [
        ('zl','Zona Leste'),
        ('zn','Zona Norte'),
        ('zo','Zona Oeste'),
        ('zs','Zona Sul'),
        ('ct','Centro'),
]

estado_opc = [
    ('AC', 'Acre'), 
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranão'),
    ('MG', 'Minas Gerais'),
    ('MS', 'Mato Grosso do Sul'),
    ('MT', 'Mato Grosso'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PE', 'Pernanbuco'),
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
    nome = models.CharField(max_length=100)
    endereço = models.CharField (max_length=100)
    cargo  = models.CharField(max_length=100)
    estado = models.CharField(max_length=2, choices=estado_opc)
    regiao = models.CharField(max_length=200, choices= zonas)
    salario = models.CharField(max_length=50)
    qtd_vaga = models.DecimalField(max_digits=8, decimal_places=0)
    Descricao_vaga = models.TextField()
    
    def __str__(self):
        return self.empresa
    

class Usuaria(models.Model):
    usuaria = models.CharField(max_length=20)
    senha = models.CharField(max_length=20)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=14)
    nascimento = models.DateField()

    def __str__(self):
        return self.usuaria