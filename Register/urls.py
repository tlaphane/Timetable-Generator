from django.conf.urls import url
from Register import views
from View_Timetable import views


urlpatterns = [

    url(r'^$', views.login, name='login'),

    url(r'^$', views.timetable ,name='table'),

    url(r'^register', views.register, name='register'),

    url(r'^reg', views.Reg,name= 'Reg'),

    url(r'^logged', views.login,name='L_I'),

   # url(r'^logged', views.login, name='confirm_log'),

    #url(r'^courses', views.courses, name='courses'),

    url(r'^forgot', views.forgot,name='forgot'),

    #url(r'^reset-password', views.resetp,name='reset'),

    #url(r'^(?P<STDN>[0-9]+)/announcement', views.astudent,name='astd'),



    #url(r'^(?P<STDN>[0-9]+)/courses', views.courses, name='course'),

    # url(r'^reset-password/reset', views.resetp)

    # login/StudentNumber/

    #url(r'^(?P<STDN>[0-9]+)', views.dummy,name= 'dum'),

    #url(r'^staff(?P<Staff_No>[0-9]+)/courses', views.StaffCourses,name = 'SC'),
    #url(r'^staff(?P<Staff_No>[0-9]+)/announcement', views.astaff,name ='astaff'),

    #url(r'^staff(?P<Staff_No>[0-9]+)/made_announcement', views.makeAnnouncement,name ='mka'),


    #url(r'^staff(?P<Staff_No>[0-9]+)', views.staff,name ='s'),

    #url(r'^staff(?P<Staff_No>[0-9]+)/courses', views.StaffCourses),

]

