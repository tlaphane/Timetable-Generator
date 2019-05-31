
from django.test import TestCase,Client
from django.urls import reverse, resolve


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.make = reverse('make',args=[200])


    def test_MAl(self):
        response = self.client.get(self.make)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Register/Make_Announcement.html')
