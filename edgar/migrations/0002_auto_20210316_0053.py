# Generated by Django 3.0.5 on 2021-03-16 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edgar', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='security',
            options={'ordering': ['securityName']},
        ),
    ]
