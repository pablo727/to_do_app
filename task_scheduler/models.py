from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone


class TaskScheduler(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    scheduled_time = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.title} @ {self.scheduled_time.strftime('%Y-%m-%d %H:%M')}"

    def get_absolute_url(self):
        return reverse("task_scheduler_detail", kwargs={"pk": self.pk})
