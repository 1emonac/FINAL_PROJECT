# Generated by Django 4.1.13 on 2024-06-11 01:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("survey", "0014_alter_pred_positive_survey_alter_pred_predict_proba_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pred",
            name="positive_survey",
            field=models.SmallIntegerField(verbose_name="긍정의 강도"),
        ),
        migrations.AlterField(
            model_name="pred",
            name="predict",
            field=models.SmallIntegerField(verbose_name="결과"),
        ),
        migrations.AlterField(
            model_name="pred",
            name="predict_proba",
            field=models.SmallIntegerField(verbose_name="잘 잤을 확률"),
        ),
        migrations.AlterField(
            model_name="pred",
            name="sleep_survey",
            field=models.SmallIntegerField(verbose_name="숙면여부"),
        ),
        migrations.AlterField(
            model_name="pred",
            name="stress_survey",
            field=models.SmallIntegerField(verbose_name="스트레스의 강도"),
        ),
    ]
