# Generated by Django 5.0.2 on 2024-03-26 17:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0003_rename_imdb_pkts_film_imdb_points_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='aktor',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aktorzy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='extrainfo',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='einfo', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='film',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='filmy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ocena',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='oceny', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='extrainfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Inne'), (4, 'Dramat'), (1, 'Horror'), (3, 'Sci-fi'), (2, 'Komedia')], null=True),
        ),
    ]
