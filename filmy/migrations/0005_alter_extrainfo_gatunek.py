# Generated by Django 5.0.2 on 2024-04-16 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0004_aktor_owner_extrainfo_owner_film_owner_ocena_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(3, 'Sci-fi'), (4, 'Dramat'), (2, 'Komedia'), (1, 'Horror'), (0, 'Inne')], null=True),
        ),
    ]
