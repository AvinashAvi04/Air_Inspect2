# Generated by Django 4.2.13 on 2024-05-18 22:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bot", "0007_bot_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="bot",
            name="bot_username",
            field=models.CharField(
                blank=True, default=None, max_length=1024, null=True
            ),
        ),
    ]