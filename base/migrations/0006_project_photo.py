# Generated by Django 5.0.2 on 2024-04-17 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0005_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="photo",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
