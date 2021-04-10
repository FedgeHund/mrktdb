# Generated by Django 3.0.5 on 2021-04-10 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('edgar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuarterlyFilerView',
            fields=[
                ('quarter', models.IntegerField(blank=True)),
                ('filerName', models.TextField(blank=True)),
                ('cik', models.TextField(blank=True)),
                ('filerType', models.TextField(blank=True)),
                ('marketValue', models.FloatField(blank=True)),
                ('previousMarketValue', models.FloatField(blank=True)),
                ('previousHoldingsCount', models.FloatField(blank=True)),
                ('newHoldingsCount', models.FloatField(blank=True)),
                ('increasedHoldingsCount', models.FloatField(blank=True)),
                ('decreasedHoldingsCount', models.FloatField(blank=True)),
                ('soldOutHoldingsCount', models.FloatField(blank=True)),
                ('top10HoldingsPercent', models.FloatField(blank=True)),
                ('averageHoldingPeriod', models.FloatField(blank=True)),
                ('filerDescription', models.TextField(blank=True)),
                ('quarterlyFilerViewId', models.AutoField(primary_key=True, serialize=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(blank=True, default=None)),
                ('deletedAt', models.DateTimeField(blank=True, default=None)),
                ('filerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edgar.Filer')),
            ],
            options={
                'ordering': ['createdAt'],
            },
        ),
    ]
