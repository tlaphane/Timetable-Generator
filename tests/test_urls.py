"""""
from django.test import SimpleTestCase ,TestCase
from django.urls import reverse, resolve
from Register.views import login,register,forgot

from Courses.views import courses
import unittest


class TestUrls(unittest.TestCase):

    def test_login_url_resolved(self):
        url = reverse('login')

        self.assertEqual(url, '/login/')


   # def test_register_url_resolved(self):
    #    url = reverse('register')
        #
     #   self.assertEquals(resolve(url).func,register)

  #  def test_Confirm_log(self):
   #     url = reverse('courses')
    #    self.assertEquals(resolve(url).func,courses)





    def  test_astd(self):
        url = reverse('astd',args=[1988])
        self.assertEqual(url,'/login/1988/announcement')

    def  test_asd(self):
        url = reverse('course',args=[1988])
        self.assertEqual(url,'/logged/1988/courses')



if __name__ == '__init__':
    unittest.main()
"""



