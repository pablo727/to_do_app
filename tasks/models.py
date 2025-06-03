from django.db import models
from django.urls import reverse


class TaskItem(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("task_detail", kwargs={"pk": self.pk})
