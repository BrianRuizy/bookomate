from django.test import TestCase
from django.urls import reverse


class TestCalendarView(TestCase):
    def test_access(self):
        response = self.client.get(reverse('home'), follow=True)
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('calendar_view'), follow=True)
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('calendar_view', kwargs={'year': 2020, 'month': 10}), follow=True)
        self.assertEqual(response.status_code, 200)


class TestNotExistingView(TestCase):
    def setUp(self) -> None:
        self.not_existed_urls = [
            "test/test1/test2",
            "test2",
            "calendarium"
        ]

    def test_404(self):
        for url in self.not_existed_urls:
            response = self.client.get(url, follow=True)
            self.assertEqual(response.status_code, 404)
