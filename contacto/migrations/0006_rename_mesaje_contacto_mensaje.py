# Generated by Django 4.0.1 on 2022-01-25 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0005_contacto_delete_contactos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacto',
            old_name='Mesaje',
            new_name='Mensaje',
        ),
    ]
