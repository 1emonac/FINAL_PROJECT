# Generated by Django 4.1.13 on 2024-06-10 05:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("survey", "0008_rename_created_pred_date"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Pred",
        ),
    ]