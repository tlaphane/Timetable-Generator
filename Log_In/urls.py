from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include,url

urlpatterns = [

    url(r'^$', views.login, name='login'),

    url(r'^logged', views.login, name='L_I'),

    url(r'^staff(?P<Staff_No>[0-9]+)/courses', include('Courses.url'), name='SC'),
    url(r'^(?P<STDN>[0-9]+)/courses', include('Courses.urls'), name='course'),
    url(r'^(?P<STDN>[0-9]+)/announcement', include('Announcements.urls'), name='astd'),
    url(r'^staff(?P<Staff_No>[0-9]+)/announcement', include('Announcements.url'), name='astaff'),

    url(r'^staff(?P<Staff_No>[0-9]+)/announcement', include('Announcements.url')),

    url(r'^staff(?P<Staff_No>[0-9]+)/make_announcement', include('Make_Announcements.url'), name='make'),
    url(r'^staff(?P<Staff_No>[0-9]+)/made_announcement', include('Make_Announcements.urls'), name='Ma'),

    # login/StudentNumber/

    url(r'^(?P<STDN>[0-9]+)', views.dummy, name='dum'),

    url(r'^staff(?P<Staff_No>[0-9]+)', views.staff, name='s'),

]
#if settings.DEBUG:
 #   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)