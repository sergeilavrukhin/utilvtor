# Generated by Django 3.2.8 on 2021-11-15 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dicts', '0003_auto_20211111_0238'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aggregation',
            options={'verbose_name': 'Агрегатное состояние отхода', 'verbose_name_plural': 'Агрегатные состояния отхода'},
        ),
        migrations.AlterModelOptions(
            name='wastecodecategory',
            options={'verbose_name': 'Классы отхода', 'verbose_name_plural': 'Классы отхода'},
        ),
        migrations.AddField(
            model_name='regions',
            name='code',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='wastecodecategory',
            name='code',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
