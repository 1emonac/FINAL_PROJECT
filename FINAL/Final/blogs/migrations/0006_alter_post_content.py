# Generated by Django 4.2.13 on 2024-06-09 01:31

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blogs", "0005_post_reference"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
    ]