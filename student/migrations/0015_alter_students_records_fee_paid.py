# Generated by Django 5.2 on 2025-04-26 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0014_alter_students_records_fee_paid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="students_records",
            name="fee_paid",
            field=models.IntegerField(blank=True, default=0, max_length=10, null=True),
        ),
    ]
