# Generated by Django 5.0.6 on 2024-08-15 11:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField(blank=True, null=True)),
                ('fat', models.FloatField(blank=True, null=True)),
                ('tbw', models.FloatField(blank=True, null=True, verbose_name='Total Body Water')),
                ('bmi', models.FloatField(blank=True, null=True, verbose_name='Body Mass Index')),
                ('muscle_mass', models.FloatField(blank=True, null=True)),
                ('bone_density', models.FloatField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
