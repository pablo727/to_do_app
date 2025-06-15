from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import TaskScheduler


class TaskSchedulerListView(ListView):
    model = TaskScheduler
    template_name = "taskscheduler_list.html"


class TaskSchedulerDetailView(DetailView):
    model = TaskScheduler
    template_name = "taskscheduler_detail.html"


class TaskSchedulerUpdateView(UpdateView):
    model = TaskScheduler
    fields = (
        "title",
        "description",
        "completed",
        "scheduled_time",
    )
    template_name = "taskscheduler_edit.html"


class TaskSchedulerDeleteView(DeleteView):
    model = TaskScheduler
    template_name = "taskscheduler_delete.html"
    success_url = reverse_lazy("taskscheduler_list")


class TaskSchedulerCreateView(CreateView):
    model = TaskScheduler
    template_name = "taskscheduler_new.html"
    fields = (
        "title",
        "description",
        "scheduled_time",
        "completed",
        "author",
    )
