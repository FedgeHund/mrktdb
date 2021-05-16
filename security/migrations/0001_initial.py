# Generated by Django 3.0.5 on 2021-04-08 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('edgar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(blank=True)),
                ('quarter', models.IntegerField(blank=True)),
                ('cusip', models.TextField(blank=True)),
                ('name', models.TextField(blank=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(blank=True, default=None)),
                ('deletedAt', models.DateTimeField(blank=True, default=None)),
                ('securityId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edgar.Security')),
            ],
            options={
                'ordering': ['createdAt'],
            },
        ),
    ]