# Generated by Django 3.0.5 on 2020-10-04 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edgar', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='security',
            options={'ordering': ['ticker'], 'verbose_name_plural': 'Securities'},
        ),
    ]