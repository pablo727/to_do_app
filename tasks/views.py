from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import TaskItem


class TasksListView(LoginRequiredMixin, ListView):
    model = TaskItem
    template_name = "home.html"


class TasksDetailView(LoginRequiredMixin, DetailView):
    model = TaskItem
    template_name = "task_detail.html"


class TasksCreateView(LoginRequiredMixin, CreateView):
    model = TaskItem
    template_name = "task_new.html"
    fields = ["title", "description"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TasksUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = TaskItem
    template_name = "task_edit.html"
    fields = ["title", "description"]

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class TasksDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = TaskItem
    template_name = "task_delete.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
