# Generated by Django 4.2.3 on 2024-03-22 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysisActions', '0006_alter_cedear_simbolo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cedear',
            name='tendencia',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
