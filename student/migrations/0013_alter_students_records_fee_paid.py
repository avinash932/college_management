# Generated by Django 5.2 on 2025-04-26 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0012_alter_students_records_fee_total"),
    ]

    operations = [
        migrations.AlterField(
            model_name="students_records",
            name="fee_paid",
            field=models.IntegerField(default=0, max_length=9),
        ),
    ]
