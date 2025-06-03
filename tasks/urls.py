from django.urls import path
from .views import TasksListView, TasksDetailView


urlpatterns = [
    path("task/<int:pk>/", TasksDetailView.as_view(), name="task_detail"),
    path("", TasksListView.as_view(), name="home"),
]
