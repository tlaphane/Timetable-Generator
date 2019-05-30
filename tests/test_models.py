#from django.test import TestCase
import pytest
#from Register.models import StudentsRegister,Login
#from Courses.models import Courses
#from Announcements.models import Announcements

#from django.utils import timezone


#class EntryModelTest(TestCase):

 #   def create_whatever(self, Student_No = 123,
  #                            Name = 'ask',
   #                           Email = 's@mail.com',
    #                          Password = 'abc123',

     #                   ):

      #  return StudentsRegister.objects.create( Student_No =Student_No ,
       #                                         Name =Name ,
        #                                        Email =Email ,
         #                                       Password =Password ,

          #                                      )

   # def create_course(self,Course_Code = 'Coms203',
    #                       Course_Name ='SD'
     #                 ):
      #  return Courses.objects.create(Course_Code =Course_Code ,
       #                               Course_Name =Course_Name
        #                             )

    #def create_Announcement(self, Course_Code = Courses(Course_Code='Coms203'),

     #                             Title = 'seven',
      #                            Content = 'testing'
       #                    ):

        #return Announcements.objects.create(Course_Code =Course_Code,

         #                                   Title =Title,
          #                                  Content =Content,
           #                                 Created = timezone.now()
            #                                )









    #def create_Login(self, Student_No = StudentsRegister(Student_No =123),
     #                      Password ='123'
      #                  ):
       # Login.save(Student_No)
        #return Login(Student_No =Student_No,
         #                           Password =Password
          #                                 )



    #def test_Register(self):
     #   entry = StudentsRegister(Name ="my name")
      #  self.assertEqual(str(entry),entry.Name)

    #def test_login(self):
     #   entry = Login(Password ="my ps")
      #  self.assertEqual(str(entry),entry.Password)



    #def test_Courses(self):

     #   s = self.create_course()
      #  self.assertTrue(isinstance(s, Courses))
       # self.assertEqual(s.__str__(),s.Course_Code)


    #def test_Announcement(self):

     #  t = self.create_Announcement()
      # self.assertTrue(isinstance(t, Announcements))
       #self.assertEqual(str(t), t.Title)





