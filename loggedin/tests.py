from django.test import TestCase
from django.urls import reverse, resolve
from django.apps import apps
from loggedin.apps import LoggedinConfig

class TestViews(TestCase):

    def setUp(self):
        self.dummy = reverse('log')

    def test_dum(self):
        response = self.client.get(self.dummy)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Register/Loggedin.html')

    def test_app(self):
        self.assertEqual(LoggedinConfig.name, 'loggedin')
        self.assertEqual(apps.get_app_config('loggedin').name, 'loggedin')
