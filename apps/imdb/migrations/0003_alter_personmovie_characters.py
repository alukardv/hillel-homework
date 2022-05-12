# Generated by Django 4.0.2 on 2022-04-04 16:08

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("imdb", "0002_alter_person_birth_date_alter_person_death_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="personmovie",
            name="characters",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=255),
                null=True,
                size=None,
                verbose_name="Characters",
            ),
        ),
    ]
