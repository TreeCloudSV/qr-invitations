# Generated by Django 2.2 on 2019-11-11 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0007_auto_20191108_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='participante',
            name='direccion',
            field=models.CharField(default='Default address', max_length=255, verbose_name='Dirección'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participante',
            name='giro',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Giro'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email'),
        ),
    ]
