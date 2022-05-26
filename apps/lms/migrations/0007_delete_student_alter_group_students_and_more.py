# Generated by Django 4.0.3 on 2022-03-25 17:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("lms", "0006_alter_group_students_alter_lesson_group"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Student",
        ),
        migrations.AlterField(
            model_name="group",
            name="students",
            field=models.ManyToManyField(
                related_name="studying_groups", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="group",
            name="teacher",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="teaching_groups",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.DeleteModel(
            name="Teacher",
        ),
    ]
