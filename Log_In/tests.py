from django.test import TestCase,Client
from django.urls import reverse, resolve
from django.apps import apps
from Log_In.apps import Log_InConfig


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

        self.login_url = reverse('login')
        self.L_I = reverse('L_I')
        self.dummy = reverse('dum', args=[100])
        self.s = reverse('s', args=[10])

    def test_dum(self):
        response = self.client.get(self.dummy)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Register/Log_in.html')

    def test_project_login_GET(self):
        response = self.client.get(self.login_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Register/Log_in.html')

    def test_re(self):
        response = self.client.get(self.L_I)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Register/Log_in.html')

    def test_staff(self):
        response = self.client.get(self.s)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Register/lecturer_page.html')

    def test_apps(self):
        self.assertEqual(Log_InConfig.name, 'Log_In')
        self.assertEqual(apps.get_app_config('Log_In').name, 'Log_In')

