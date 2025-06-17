from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse

from .models import TaskScheduler
from .forms import CommentForm


class TaskSchedulerListView(LoginRequiredMixin, ListView):
    model = TaskScheduler
    template_name = "taskscheduler_list.html"


class CommentGet(DetailView):
    model = TaskScheduler
    template_name = "taskscheduler_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class CommentPost(SingleObjectMixin, FormView):
    model = TaskScheduler
    form_class = CommentForm
    template_name = "taskscheduler_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.taskscheduler = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        taskscheduler = self.object
        return reverse("task_scheduler_detail", kwargs={"pk": taskscheduler.pk})


class TaskSchedulerDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)


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
