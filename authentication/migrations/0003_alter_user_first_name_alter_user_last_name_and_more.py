# Generated by Django 5.0.6 on 2024-05-15 14:22

import commons.constants
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0002_user_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(blank=True, null=True, verbose_name="First Name"),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(blank=True, null=True, verbose_name="Last Name"),
        ),
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[
                    ("PATIENT", "Patient"),
                    ("DOCTOR", "Doctor"),
                    ("SENIOR_DOCTOR", "Senior Doctor"),
                ],
                default=commons.constants.UserRoles["PATIENT"],
            ),
        ),
    ]
