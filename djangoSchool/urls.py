"""djangoSchool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Add an import:  from blog import urls as blog_urls
	2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.contrib.auth.views import login, logout
from rest_framework import routers
from mywrapper.jwt_utils import get_token_with_password


urlpatterns = [
	url(r'^$','djangoSchool.views.home',name="home"),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^attendance/',include('attendance.urls', namespace="attendance")),
	url(r'^notice/',include('notice.urls', namespace="notice")),
	url(r'^marks/',include('marks.urls', namespace="marks")),
	url(r'^accounts/', include('accounts.urls',namespace="accounts")),
	url(r'^records/', include('records.urls',namespace="records")),
	url(r'^myapi/', include('mywrapper.urls',namespace="mywrapper")),
	url(r'^docs/', include('rest_framework_swagger.urls')),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^api-token-auth/', get_token_with_password),
	url(r'^user/password/reset/$', 
		'django.contrib.auth.views.password_reset', 
		{'post_reset_redirect' : '/user/password/reset/done/'},
		name="password_reset"),
	url(r'^user/password/reset/done/$',
		'django.contrib.auth.views.password_reset_done',name="password_reset_done"),
	url(r'^user/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 
		'django.contrib.auth.views.password_reset_confirm', 
		{'post_reset_redirect' : '/user/password/done/'},name="password_reset_confirm"),
	url(r'^user/password/done/$', 
		'django.contrib.auth.views.password_reset_complete'),
	url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='reset'),
]