# Generated by Django 4.1.13 on 2024-06-10 06:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("survey", "0011_delete_pred"),
    ]

    operations = [
        migrations.CreateModel(
            name="Pred",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user", models.CharField(max_length=255)),
                ("predict", models.TextField(max_length=1, verbose_name="결과")),
                (
                    "predict_proba",
                    models.TextField(max_length=2, verbose_name="잘 잤을 확률"),
                ),
                ("sleep_survey", models.TextField(max_length=1, verbose_name="숙면여부")),
                (
                    "stress_survey",
                    models.TextField(max_length=1, verbose_name="스트레스의 강도"),
                ),
                (
                    "positive_survey",
                    models.TextField(max_length=1, verbose_name="긍정의 강도"),
                ),
                ("date", models.DateField(auto_now_add=True, verbose_name="일자")),
            ],
        ),
    ]
