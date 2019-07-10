# Generated by Django 2.2.3 on 2019-07-10 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190705_1839'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('senha', models.CharField(max_length=8)),
            ],
        ),
        migrations.RemoveField(
            model_name='empresas',
            name='empresa',
        ),
        migrations.AddField(
            model_name='empresas',
            name='endereço',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='empresas',
            name='nome',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='empresas',
            name='cargo',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='empresas',
            name='estado',
            field=models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranão'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PE', 'Pernanbuco'), ('PI', 'Piauí'), ('PR', 'Paraná'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins')], default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='empresas',
            name='qtd_vaga',
            field=models.DecimalField(decimal_places=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='empresas',
            name='regiao',
            field=models.CharField(choices=[('zl', 'Zona Leste'), ('zn', 'Zona Norte'), ('zo', 'Zona Oeste'), ('zs', 'Zona Sul'), ('ct', 'Centro')], default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='empresas',
            name='salario',
            field=models.CharField(default='', max_length=50),
        ),
    ]
