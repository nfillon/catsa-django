# Generated by Django 4.0.1 on 2022-01-24 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactos',
            name='Asunto',
            field=models.TextField(max_length=200),
        ),
    ]