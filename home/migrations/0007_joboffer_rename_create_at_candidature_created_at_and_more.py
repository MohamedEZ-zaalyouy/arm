# Generated by Django 5.1.2 on 2024-11-11 10:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_magasin'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=500)),
                ('employment_type', models.CharField(choices=[('Temps plein', 'Full-time'), ('Temps partiel', 'Part-time')], default='Temps plein', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameField(
            model_name='candidature',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='candidature',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.RemoveField(
            model_name='candidature',
            name='employment_type',
        ),
        migrations.AddField(
            model_name='candidature',
            name='job_offer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candidatures', to='home.joboffer'),
        ),
    ]