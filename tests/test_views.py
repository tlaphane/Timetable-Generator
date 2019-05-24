from django.test import TestCase,Client
from django.urls import reverse, resolve
from Register.models import Courses
import pytest


class TestViews(TestCase):
        def setUp(self):
            self.client = Client()
            self.login_url = reverse('login')
            self.confirm_log = reverse('confirm_log')
            self.reset = reverse('reset')
            self.forgot = reverse('forgot')
            self.Reg = reverse('register')
            self.astd = reverse('astd',args=[1988])
            self.make = reverse('make', args=[200])
            self.SC = reverse('SC',args=[100])
            self.mk = reverse('astaff',args=[100])
            self.dummy = reverse('dum',args=[100])
            self.s = reverse('s',args =[10])
            self.c= reverse('course',args=[133])
            self.r = reverse('Reg')
            self.m_A = reverse('mka',args=[100])

        def test_ma(self):
            response = self.client.get(self.m_A)
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'Register/Announcements.html')

        def test_re(self):
            response = self.client.get(self.r)
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'Register/Log_in.html')

        def test_c(self):
            response = self.client.get(self.c)
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'Register/Courses.html')

        def test_staff(self):
            response = self.client.get(self.s)
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'Register/lecturer_page.html')

        def test_dum(self):
            response = self.client.get(self.dummy)
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'Register/Loggedin.html')


        def test_SC(self):
            response = self.client.get(self.SC)
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'Register/Courses.html')


        def test_make(self):
            response = self.client.get(self.make)
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'Register/Make_Announcement.html')

        def test_stuff(self):
            response = self.client.get(self.mk)
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'Register/View_announcement.html')

        def test_astd_GET(self):

            response = self.client.get(self.astd)
            self.assertEquals(response.status_code,200)
            self.assertTemplateUsed(response,'Register/View_announcement.html')

        def  test_project_login_GET(self):

             response = self.client.get(self.login_url)

             self.assertEquals(response.status_code, 200)
             self.assertTemplateUsed(response, 'Register/Log_in.html')

        def test_project_confirmlogin_GET(self):
            response = self.client.get(self.confirm_log)

            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'Register/Log_in.html')

        def test_forgot_GET(self):
            response = self.client.get(self.forgot)

            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'Register/forgot.html')

        def test_reset_GET(self):

            response = self.client.get(self.reset)
            self.assertEquals(response.status_code,200)
            self.assertTemplateUsed(response,'Register/reset.html')

        def test_reg_GET(self):
            response = self.client.get(self.Reg)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'Register/register.html')




