# Generated by Django 3.0.5 on 2021-02-07 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edgar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='security',
            name='cikCusipMappingId',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]