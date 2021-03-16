# Generated by Django 3.0.5 on 2021-03-15 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('edgar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('quarter', models.IntegerField(blank=True)),
                ('securityName', models.TextField(blank=True)),
                ('filerName', models.TextField(blank=True)),
                ('investmentDiscretion', models.TextField(blank=True)),
                ('quantity', models.FloatField(blank=True)),
                ('marketValue', models.FloatField(blank=True)),
                ('weightPercent', models.FloatField(blank=True)),
                ('previousWeightPercent', models.FloatField(blank=True)),
                ('estimatedAverageCost', models.FloatField(blank=True)),
                ('lastPrice', models.FloatField(blank=True)),
                ('estimatedProfit', models.FloatField(blank=True)),
                ('ranking', models.FloatField(blank=True)),
                ('changeInShares', models.FloatField(blank=True)),
                ('changeInPositionPercent', models.FloatField(blank=True)),
                ('sourceType', models.TextField(blank=True)),
                ('sourcedOn', models.DateTimeField(blank=True)),
                ('positionType', models.TextField(blank=True)),
                ('positionId', models.AutoField(primary_key=True, serialize=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(blank=True, default=None)),
                ('deletedAt', models.DateTimeField(blank=True, default=None)),
                ('quarterFirstOwned', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quarterFirstOwned_Id', to='edgar.QuarterlyHolding')),
                ('quarterId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quarter_Id', to='edgar.QuarterlyHolding')),
                ('securityId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edgar.Security')),
            ],
            options={
                'ordering': ['createdAt'],
            },
        ),
    ]
