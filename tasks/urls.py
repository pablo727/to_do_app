from django.urls import path
from .views import (
    TasksListView,
    TasksDetailView,
    TasksCreateView,
    TasksUpdateView,
    TasksDeleteView,
)

urlpatterns = [
    path("task/new/", TasksCreateView.as_view(), name="task_new"),
    path("task/<int:pk>/", TasksDetailView.as_view(), name="task_detail"),
    path("task/<int:pk>/edit/", TasksUpdateView.as_view(), name="task_edit"),
    path("task/<int:pk>/delete/", TasksDeleteView.as_view(), name="task_delete"),
    path("", TasksListView.as_view(), name="home"),
]
