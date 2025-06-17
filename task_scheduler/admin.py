from django.contrib import admin
from .models import TaskScheduler, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class TaskSchedulerAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
    list_display = [
        "title",
        "description",
        "author",
        "completed",
        "scheduled_time",
    ]


admin.site.register(TaskScheduler, TaskSchedulerAdmin)
admin.site.register(Comment)
