# Generated by Django 4.1.1 on 2022-10-20 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0003_doctor_receptions"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctor",
            name="type",
            field=models.CharField(
                choices=[
                    ("Пользователь", "Client"),
                    ("ЛОР", "Доктор-лор"),
                    ("Терапевт", "Доктор-терапевт"),
                ],
                default="Пользователь",
                max_length=50,
            ),
        ),
        migrations.CreateModel(
            name="AvailableTime",
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
                ("date", models.DateField()),
                ("time", models.TimeField()),
                ("is_active", models.BooleanField()),
                ("doctor", models.ManyToManyField(to="base.doctor")),
            ],
        ),
    ]
