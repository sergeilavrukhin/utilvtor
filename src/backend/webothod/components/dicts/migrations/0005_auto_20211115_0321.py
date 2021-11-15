# Generated by Django 3.2.8 on 2021-11-15 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dicts', '0004_auto_20211115_0316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regions',
            name='activity',
        ),
        migrations.RemoveField(
            model_name='regions',
            name='iso',
        ),
        migrations.AlterField(
            model_name='regions',
            name='code',
            field=models.PositiveIntegerField(default=0, verbose_name='Код региона'),
        ),
        migrations.AlterField(
            model_name='wastecodecategory',
            name='code',
            field=models.PositiveIntegerField(default=0, verbose_name='Класс отхода'),
        ),
    ]
