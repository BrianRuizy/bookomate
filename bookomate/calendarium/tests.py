from django.test import TestCase


class TestCalendarView(TestCase):
    def test_access(self):
        response = self.client.get('', follow=True)
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
