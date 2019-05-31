from django.test import TestCase,Client
from django.urls import reverse, resolve
from django.apps import apps
from Courses.apps import CoursesConfig


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

    def test_apps(self):
        self.assertEqual(CoursesConfig.name, 'Courses')
        self.assertEqual(apps.get_app_config('Courses').name, 'Courses')
