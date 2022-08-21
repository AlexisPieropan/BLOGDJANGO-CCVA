# Generated by Django 4.0.6 on 2022-08-20 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Domicilio'),
        ),
        migrations.AddField(
            model_name='user',
            name='dni',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='DNI'),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('SOCIO', 'Socio'), ('VISITIANTE', 'Visitante')], default='VISITIANTE', max_length=12, verbose_name='Role'),
        ),
    ]
