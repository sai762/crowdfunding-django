# Generated by Django 5.0.2 on 2024-04-26 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0007_alter_project_photo"),
    ]

    operations = [
        migrations.AddField(
            model_name="creator",
            name="fund_collected",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
