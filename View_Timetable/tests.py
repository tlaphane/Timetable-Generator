from django.test import TestCase,Client
from django.urls import reverse, resolve


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.a = reverse('table')

    def test_MA(self):
        response = self.client.get(self.a)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Register/Timetable.html')

