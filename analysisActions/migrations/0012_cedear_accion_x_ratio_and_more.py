# Generated by Django 5.0.3 on 2024-04-01 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysisActions', '0011_operacion_alter_accion_recomendacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='cedear',
            name='accion_x_ratio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='cedear',
            name='beneficio_diferencia_accion',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]