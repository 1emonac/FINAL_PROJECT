# Generated by Django 4.1.13 on 2024-05-29 03:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="profile_image",
        ),
        migrations.RemoveField(
            model_name="user",
            name="short_description",
        ),
    ]
