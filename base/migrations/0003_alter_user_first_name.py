# Generated by Django 4.1.1 on 2022-10-01 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_alter_user_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(default="Test", max_length=255),
        ),
    ]