# Generated by Django 4.0.1 on 2022-02-20 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0011_alter_proyectocliente_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='proyectos'),
        ),
        migrations.DeleteModel(
            name='ProyectoCliente',
        ),
    ]
