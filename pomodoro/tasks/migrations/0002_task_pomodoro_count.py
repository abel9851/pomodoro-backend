# Generated by Django 4.2.6 on 2023-12-11 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="pomodoro_count",
            field=models.IntegerField(default=1, verbose_name="task pomodoro count"),
        ),
    ]
