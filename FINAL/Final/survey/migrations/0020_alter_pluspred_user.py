# Generated by Django 4.1.13 on 2024-06-11 06:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("survey", "0019_alter_pluspred_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pluspred",
            name="user",
            field=models.CharField(max_length=255),
        ),
    ]