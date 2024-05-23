# Generated by Django 5.0.2 on 2024-02-20 02:48

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DongID",
            fields=[
                (
                    "address_code",
                    models.CharField(
                        max_length=8,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="지역코드",
                    ),
                ),
                ("si_name", models.CharField(max_length=5, verbose_name="시 이름")),
                ("gu_name", models.CharField(max_length=10, verbose_name="구 이름")),
                ("dong_name", models.CharField(max_length=10, verbose_name="동 이름")),
                ("x_cordinate", models.CharField(max_length=20, verbose_name="x좌표")),
                ("y_cordinate", models.CharField(max_length=20, verbose_name="y좌표")),
            ],
        ),
    ]
