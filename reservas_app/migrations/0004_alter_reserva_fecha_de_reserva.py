# Generated by Django 4.1 on 2022-10-28 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas_app', '0003_alter_reserva_cantidad_de_personas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='fecha_de_reserva',
            field=models.DateField(help_text='aa/mm/dd'),
        ),
    ]
