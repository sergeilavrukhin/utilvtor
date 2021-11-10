# Generated by Django 3.2.8 on 2021-11-10 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dicts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('itn', models.CharField(max_length=12)),
                ('latitude', models.CharField(max_length=20, null=True)),
                ('longitude', models.CharField(max_length=20, null=True)),
                ('phones', models.CharField(max_length=600)),
                ('emails', models.CharField(max_length=600)),
                ('site', models.CharField(max_length=255)),
                ('activity', models.CharField(max_length=600)),
                ('locality', models.CharField(max_length=600)),
                ('gps', models.CharField(max_length=255)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regions', to='dicts.regions', verbose_name='Регион')),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
                'db_table': 'companies',
            },
        ),
    ]
