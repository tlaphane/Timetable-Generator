""""
from django.test import TestCase,Client
from django.urls import reverse, resolve


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

        self.ma = reverse('Maa')
        self.make = reverse('make', args=[200])

    def test_MA(self):
        response = self.client.get(self.ma)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Register/Announcement.html')


    def test_MAl(self):
        response = self.client.get(self.make)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'login/staff222/made_announcement')
"""""