# Generated by Django 2.2.3 on 2019-07-12 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20190710_1521'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.RemoveField(
            model_name='empresas',
            name='regiao',
        ),
    ]
