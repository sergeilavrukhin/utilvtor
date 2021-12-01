# Generated by Django 3.2.8 on 2021-12-01 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dicts', '0006_aggregation_code'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='regions',
            index=models.Index(fields=['code'], name='regions_code_aa1ecb_idx'),
        ),
    ]
