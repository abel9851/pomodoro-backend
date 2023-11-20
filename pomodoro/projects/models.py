from core import models as core_models

from django.conf import settings
from django.db import models


class Project(core_models.TimeStampedModel):
    """Project Model Definition"""

    class Meta:
        db_table = "projects"

    name = models.CharField(verbose_name="project name", max_length=200)
    # TODO: django doc
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="related user",
        related_name="projects",
        on_delete=models.CASCADE,
    )
    tasks = models.ManyToManyField(
        "tasks.Task",
        verbose_name="related tasks",
        related_name="projects",
        through="ProjectTaskAssociation",
    )
    description = models.CharField(
        verbose_name="project description", max_length=300, default="", blank=True
    )
    color = models.CharField(
        verbose_name="color code", max_length=150, default="#0067c0"
    )
    is_active = models.BooleanField(verbose_name="project 활성화 여부")


class ProjectTaskAssociation(core_models.TimeStampedModel):
    """Project Task Association Model Definition"""

    class Meta:
        db_table = "project_task_associations"

    project = models.ForeignKey(
        "Project",
        verbose_name="related project",
        related_name="task_association",
        on_delete=models.CASCADE,
    )
    task = models.ForeignKey(
        "tasks.Task",
        verbose_name="related task",
        related_name="project_association",
        on_delete=models.CASCADE,
    )
