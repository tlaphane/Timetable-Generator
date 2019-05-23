from django.test import SimpleTestCase ,TestCase
from django.core.urlresolvers import reverse, resolve
from Register.views import login,register,courses,forgot,resetp,astudent
#from Timetable.Register.views import login, register
import unittest


class TestUrls(unittest.TestCase):
    def test_login_url_resolved(self):
        url = reverse('login')

        self.assertEquals(resolve(url).func, login)


    def test_register_url_resolved(self):
        url = reverse('register')
        #
        self.assertEquals(resolve(url).func,register)

    def test_Confirm_log(self):
        url = reverse('courses')
        self.assertEquals(resolve(url).func,courses)

    def test_forgot(self):
        url = reverse('forgot')
        self.assertEquals(resolve(url).func,forgot)

    def test_reset(self):
        url = reverse('reset')
        self.assertEquals(resolve(url).func,resetp)

    def  test_astd(self):
        url = reverse('astd',args=[1988])
        self.assertEqual(url,'/login/1988/announcement')

    def  test_astd(self):
        url = reverse('course',args=[1988])
        self.assertEqual(url,'/login/1988/courses')

if __name__ == '__init__':
    unittest.main()




