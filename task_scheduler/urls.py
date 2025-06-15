from django.urls import path
from .views import (
    TaskSchedulerListView,
    TaskSchedulerDetailView,
    TaskSchedulerUpdateView,
    TaskSchedulerDeleteView,
    TaskSchedulerCreateView,
)


urlpatterns = [
    path("<int:pk>/", TaskSchedulerDetailView.as_view(), name="task_scheduler_detail"),
    path(
        "<int:pk>/edit/", TaskSchedulerUpdateView.as_view(), name="taskscheduler_edit"
    ),
    path(
        "<int:pk>/delete/",
        TaskSchedulerDeleteView.as_view(),
        name="taskscheduler_delete",
    ),
    path("new/", TaskSchedulerCreateView.as_view(), name="taskscheduler_new"),
    path("", TaskSchedulerListView.as_view(), name="taskscheduler_list"),
]
