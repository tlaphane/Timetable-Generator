from django.test import TestCase
from django.urls import reverse, resolve

class TestViews(TestCase):

    def setUp(self):
        self.dummy = reverse('log')

    def test_dum(self):
        response = self.client.get(self.dummy)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Register/Loggedin.html')