# Generated by Django 3.2.8 on 2021-11-16 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0005_alter_companywastecodes_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='locality',
            field=models.CharField(max_length=600, verbose_name='Адрес'),
        ),
    ]
