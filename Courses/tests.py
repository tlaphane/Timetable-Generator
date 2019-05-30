from django.test import TestCase,Client
from django.urls import reverse, resolve


class TestViews(TestCase):
    def setUp(self):

        self.SC = reverse('SC', args=[100])
        self.c = reverse('course', args=[133])

    def test_c(self):
        response = self.client.get(self.c)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Register/Courses.html')

    def test_SC(self):
        response = self.client.get(self.SC)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Register/Courses.html')
