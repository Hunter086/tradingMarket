# Generated by Django 4.2.3 on 2024-03-26 14:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('analysisActions', '0010_accion_recomendacion_alter_accion_simbolo_cedears'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_compra', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precio_venta', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('cantidad', models.IntegerField()),
                ('moneda', models.CharField(choices=[('USD', 'Dólar Estadounidense'), ('ARS', 'Peso Argentino')], max_length=3)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('simbolo', models.CharField(max_length=100)),
                ('monto_total', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
            options={
                'ordering': ['-fecha'],
            },
        ),
        migrations.AlterField(
            model_name='accion',
            name='recomendacion',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
