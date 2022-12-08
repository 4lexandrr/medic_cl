# Generated by Django 4.1.1 on 2022-10-23 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0006_alter_tests_cost_alter_user_email_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="useritem",
            name="user",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="useritem",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="base.tests"
            ),
        ),
    ]