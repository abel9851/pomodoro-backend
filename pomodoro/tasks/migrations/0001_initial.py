# Generated by Django 4.2.6 on 2024-01-11 15:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
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
                ("name", models.CharField(max_length=200, verbose_name="task name")),
                (
                    "memo",
                    models.CharField(
                        blank=True, default="", max_length=300, verbose_name="task memo"
                    ),
                ),
                (
                    "priority",
                    models.IntegerField(
                        choices=[(0, "HIGH"), (1, "MEDIUM"), (2, "LOW")],
                        default=1,
                        verbose_name="task priority",
                    ),
                ),
                (
                    "due_date",
                    models.DateField(
                        default=datetime.date.today, verbose_name="task due date"
                    ),
                ),
                (
                    "pomodoro_count",
                    models.IntegerField(default=1, verbose_name="task pomodoro count"),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tasks",
                        to="projects.project",
                        verbose_name="related project",
                    ),
                ),
            ],
            options={
                "db_table": "tasks",
            },
        ),
    ]
