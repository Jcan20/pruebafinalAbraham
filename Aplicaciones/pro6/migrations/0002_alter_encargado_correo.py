# Generated by Django 5.0 on 2025-02-10 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro6', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encargado',
            name='correo',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
