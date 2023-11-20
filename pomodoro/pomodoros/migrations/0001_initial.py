# Generated by Django 4.2.6 on 2023-11-20 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Pomodoro",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "pomodoro_length",
                    models.IntegerField(verbose_name="pomodoro time length"),
                ),
                ("break_length", models.IntegerField(verbose_name="break time length")),
                (
                    "tasks",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pomodoros",
                        to="tasks.task",
                        verbose_name="related task",
                    ),
                ),
            ],
            options={
                "db_table": "pomodoros",
            },
        ),
    ]
