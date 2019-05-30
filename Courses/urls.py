from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^', views.courses, name='course'),
    url(r'^(?P<STDN>[0-9]+)/courses', views.courses, name='course'),
    url(r'^staff(?P<Staff_No>[0-9]+)/courses', views.StaffCourses, name='SC'),


]

#if settings.DEBUG:
 #   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)