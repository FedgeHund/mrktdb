# Generated by Django 3.0.5 on 2020-10-04 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edgar', '0003_cikcusipmapping_cikcusipmappingid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cikcusipmapping',
            name='cikCusipMappingId',
            field=models.TextField(),
        ),
    ]