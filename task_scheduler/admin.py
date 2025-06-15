from django.contrib import admin
from .models import TaskScheduler


class TaskSchedulerAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "description",
        "author",
        "completed",
        "scheduled_time",
    ]


admin.site.register(TaskScheduler, TaskSchedulerAdmin)
