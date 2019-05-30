from django.conf.urls import url
from View_Timetable import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include,url

urlpatterns = [

    url(r'^$', views.timetable, name='table'),

]