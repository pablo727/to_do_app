from django.views.generic import ListView, DetailView
from .models import TaskItem


class TasksListView(ListView):
    model = TaskItem
    template_name = "home.html"


class TasksDetailView(DetailView):
    model = TaskItem
    template_name = "task_detail.html"
