# Generated by Django 5.2 on 2025-04-18 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0006_students_records_roll"),
    ]

    operations = [
        migrations.AlterField(
            model_name="students_records",
            name="roll",
            field=models.IntegerField(default=None, max_length=7),
        ),
    ]
