from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import TaskScheduler


class TaskSchedulerListView(LoginRequiredMixin, ListView):
    model = TaskScheduler
    template_name = "taskscheduler_list.html"


class TaskSchedulerDetailView(LoginRequiredMixin, DetailView):
    model = TaskScheduler
    template_name = "taskscheduler_detail.html"


class TaskSchedulerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = TaskScheduler
    fields = (
        "title",
        "description",
        "completed",
        "scheduled_time",
    )
    template_name = "taskscheduler_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class TaskSchedulerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = TaskScheduler
    template_name = "taskscheduler_delete.html"
    success_url = reverse_lazy("taskscheduler_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class TaskSchedulerCreateView(LoginRequiredMixin, CreateView):
    model = TaskScheduler
    template_name = "taskscheduler_new.html"
    fields = (
        "title",
        "description",
        "scheduled_time",
        "completed",
    )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
