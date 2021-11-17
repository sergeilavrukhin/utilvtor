# Generated by Django 3.2.8 on 2021-11-17 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0009_companywastecodes_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='activity',
            field=models.CharField(blank=True, max_length=600, null=True, verbose_name='Типы отходов с которыми работает'),
        ),
        migrations.AlterField(
            model_name='companies',
            name='emails',
            field=models.CharField(blank=True, max_length=600, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='companies',
            name='gps',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Координаты'),
        ),
        migrations.AlterField(
            model_name='companies',
            name='latitude',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='companies',
            name='longitude',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='companies',
            name='phones',
            field=models.CharField(blank=True, max_length=600, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='companies',
            name='site',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Сайт'),
        ),
    ]
