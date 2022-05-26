# Generated by Django 4.0.2 on 2022-03-25 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("lms", "0005_rename_class_group_lesson_group"),
    ]

    operations = [
        migrations.AlterField(
            model_name="group",
            name="students",
            field=models.ManyToManyField(to="lms.Student"),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="group",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="lessons",
                to="lms.group",
            ),
        ),
    ]
