from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^selectComponent/(?P<pk>[0-9]+)/$',views.indexComponent,name='indexComponent'),
	url(r'^viewAttendance/(?P<pk>[0-9]+)/$', views.viewAttendance, name='viewAttendance'),
	url(r'^enterAttendance/(?P<pk>[0-9]+)/$', views.enterAttendance, name='enterAttendance'),
	url(r'^uploadAttendance/(?P<pk>[0-9]+)/$', views.uploadAttendance, name='uploadAttendance'),
]