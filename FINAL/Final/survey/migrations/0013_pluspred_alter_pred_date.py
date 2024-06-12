# Generated by Django 4.1.13 on 2024-06-11 00:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("survey", "0012_pred"),
    ]

    operations = [
        migrations.CreateModel(
            name="PlusPred",
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
                ("dream_survey", models.TextField(max_length=1, verbose_name="꿈의 강도")),
                (
                    "caffeine_survey",
                    models.TextField(max_length=1, verbose_name="카페인 강도"),
                ),
                (
                    "alcohol_survey",
                    models.TextField(max_length=1, verbose_name="알코올의 강도"),
                ),
                ("talk_survey", models.TextField(max_length=1, verbose_name="대화의 강도")),
                (
                    "personalcare_survey",
                    models.TextField(max_length=1, verbose_name="개인정비의 강도"),
                ),
                (
                    "work_survey",
                    models.TextField(max_length=1, verbose_name="당일 업무 유무"),
                ),
                (
                    "home_survey",
                    models.TextField(max_length=1, verbose_name="집에서 많은 시간을 보내는지의 여부"),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="pred",
            name="date",
            field=models.DateField(auto_now_add=True, unique=True, verbose_name="일자"),
        ),
    ]
