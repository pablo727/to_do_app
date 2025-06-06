from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import TaskItem


class TasksListView(ListView):
    model = TaskItem
    template_name = "home.html"


class TasksDetailView(DetailView):
    model = TaskItem
    template_name = "task_detail.html"


class TasksCreateView(CreateView):
    model = TaskItem
    template_name = "task_new.html"
    fields = ["title", "author", "description"]


class TasksUpdateView(UpdateView):
    model = TaskItem
    template_name = "task_edit.html"
    fields = ["title", "description"]


class TasksDeleteView(DeleteView):
    model = TaskItem
    template_name = "task_delete.html"
    success_url = reverse_lazy("home")
