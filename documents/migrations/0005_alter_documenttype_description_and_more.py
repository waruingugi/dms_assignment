# Generated by Django 5.0.6 on 2024-05-15 14:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("documents", "0004_alter_historicaldocuments_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="documenttype",
            name="description",
            field=models.CharField(
                help_text="A brief description of the type of the document"
            ),
        ),
        migrations.AlterField(
            model_name="documenttype",
            name="type",
            field=models.CharField(),
        ),
    ]
