# Generated by Django 4.1.13 on 2024-06-12 00:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("survey", "0025_alter_pluspred_date_alter_pred_date"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="pred",
            options={"ordering": ["date"]},
        ),
    ]