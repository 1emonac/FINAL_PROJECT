# Generated by Django 4.1.13 on 2024-06-11 01:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("survey", "0013_pluspred_alter_pred_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pred",
            name="positive_survey",
            field=models.IntegerField(max_length=1, verbose_name="긍정의 강도"),
        ),
        migrations.AlterField(
            model_name="pred",
            name="predict_proba",
            field=models.IntegerField(max_length=2, verbose_name="잘 잤을 확률"),
        ),
        migrations.AlterField(
            model_name="pred",
            name="sleep_survey",
            field=models.IntegerField(max_length=1, verbose_name="숙면여부"),
        ),
        migrations.AlterField(
            model_name="pred",
            name="stress_survey",
            field=models.IntegerField(max_length=1, verbose_name="스트레스의 강도"),
        ),
    ]
