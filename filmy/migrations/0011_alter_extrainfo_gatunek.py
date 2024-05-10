# Generated by Django 5.0.2 on 2024-05-10 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0010_alter_extrainfo_gatunek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(2, 'Komedia'), (3, 'Sci-fi'), (1, 'Horror'), (0, 'Inne'), (4, 'Dramat')], null=True),
        ),
    ]
