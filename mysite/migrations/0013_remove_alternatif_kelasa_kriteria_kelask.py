# Generated by Django 4.1.2 on 2023-11-19 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0012_alternatif_kelasa"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="alternatif",
            name="kelasA",
        ),
        migrations.AddField(
            model_name="kriteria",
            name="kelasK",
            field=models.TextField(blank=True, null=True),
        ),
    ]
