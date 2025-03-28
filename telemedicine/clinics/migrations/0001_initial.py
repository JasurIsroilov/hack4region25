# Generated by Django 5.1.7 on 2025-03-28 00:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('clinic_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clinics', to='cities.city')),
            ],
        ),
    ]
