from django.test import TestCase,Client
from django.urls import reverse, resolve
from View_Timetable.apps import ViewTimetableConfig
from django.apps import apps

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

       # self.a = reverse('table')

    def test_app(self):
        self.assertEqual(ViewTimetableConfig.name, 'View_Timetable')
        self.assertEqual(apps.get_app_config('View_Timetable').name, 'View_Timetable')


"""""
    def test_MA(self):
        response = self.client.get(self.a)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Register/Timetable.html')
"""


