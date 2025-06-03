from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import TaskItem


class TaskItemTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret"
        )

        cls.task = TaskItem.objects.create(
            title="A good title",
            description="Nice description content",
            author=cls.user,
        )

    def test_taskitem_model(self):
        self.assertEqual(self.task.title, "A good title")
        self.assertEqual(self.task.description, "Nice description content")
        self.assertEqual(self.task.author.username, "testuser")
        self.assertEqual(str(self.task), "A good title")
        self.assertEqual(self.task.get_absolute_url(), "/task/1/")

    def test_url_exists_at_the_correct_location_listview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_the_correct_location_detailview(self):
        response = self.client.get("/task/1/")
        self.assertEqual(response.status_code, 200)

    def test_task_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nice description content")
        self.assertTemplateUsed(response, "home.html")

    def test_task_detaiview(self):
        response = self.client.get(reverse("task_detail", kwargs={"pk": self.task.pk}))
        no_response = self.client.get("/task/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "A good title")
        self.assertTemplateUsed(response, "task_detail.html")
