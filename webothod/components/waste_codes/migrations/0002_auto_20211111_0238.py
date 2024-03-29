# Generated by Django 3.2.8 on 2021-11-11 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waste_codes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wastecodes',
            name='activity',
        ),
        migrations.RemoveField(
            model_name='wastecodes',
            name='iso',
        ),
        migrations.RemoveField(
            model_name='wastecodes',
            name='url',
        ),
        migrations.AlterField(
            model_name='wastecodes',
            name='keywords',
            field=models.TextField(verbose_name='Ключевые слова'),
        ),
        migrations.AlterField(
            model_name='wastecodes',
            name='name',
            field=models.CharField(max_length=600, verbose_name='Название'),
        ),
    ]
