# Generated by Django 4.1.1 on 2022-10-01 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(default="Test", max_length=50),
        ),
    ]
