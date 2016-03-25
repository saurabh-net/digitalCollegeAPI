from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from mywrapper import views
from django.conf.urls import patterns
from django.conf.urls import include

urlpatterns = [
    
    url(r'^getteachersubjects/(?P<pk>[0-9]+)/$', views.getteachersubjects),
    url(r'^getstudentlistforcomponent/(?P<pk>[0-9]+)/$', views.getstudentlistforcomponent),
    url(r'^postabsentstudents/$', views.postabsentstudents),
    url(r'^subject/$', views.SubjectList.as_view()),
    url(r'^subject/(?P<pk>[0-9]+)/$', views.SubjectDetail.as_view()),    
    url(r'^subjectcomponents/$', views.SubjectComponentsList.as_view()),
    url(r'^subjectcomponents/(?P<pk>[0-9]+)/$', views.SubjectComponentsDetail.as_view()),
    url(r'^student/$', views.StudentList.as_view()),
    url(r'^student/(?P<pk>[0-9]+)/$', views.StudentDetail.as_view()),
    url(r'^teacher/$', views.TeacherList.as_view()),
    url(r'^teacher/(?P<pk>[0-9]+)/$', views.TeacherDetail.as_view()),
    url(r'^subjectperstudent/$', views.SubjectsPerStudentList.as_view()),
    url(r'^subjectperstudent/(?P<pk>[0-9]+)/$', views.SubjectsPerStudentDetail.as_view()),
    url(r'^subjectperteacher/$', views.SubjectsPerTeacherList.as_view()),
    url(r'^subjectperteacher/(?P<pk>[0-9]+)/$', views.SubjectsPerTeacherDetail.as_view()),
    url(r'^attendance/$', views.AttendanceList.as_view()),
    url(r'^attendance/(?P<pk>[0-9]+)/$', views.AttendanceDetail.as_view()),
    url(r'^daysattendancewastaken/$', views.DaysAttendanceWasTakenList.as_view()),
    url(r'^daysattendancewastaken/(?P<pk>[0-9]+)/$', views.DaysAttendanceWasTakenDetail.as_view()),
    url(r'^test/$', views.TestList.as_view()),
    url(r'^test/(?P<pk>[0-9]+)/$', views.TestDetail.as_view()),
    url(r'^marks/$', views.MarksList.as_view()),
    url(r'^marks/(?P<pk>[0-9]+)/$', views.MarksDetail.as_view()),
    url(r'^addstudentaccount/$', views.addstudentaccount),
    url(r'^profile/$', views.ProfileList.as_view()),
    url(r'^profile/(?P<pk>[0-9]+)/$', views.ProfileDetail.as_view()),
    url(r'^user/$', views.UserList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^getallsubjects/$', views.getallsubjects),
    url(r'^changepassword/$', views.changepassword),
    url(r'^getattendanceforsubjectcomponent/(?P<pk>[0-9]+)/$', views.getattendanceforsubjectcomponent),
    url(r'^getattendanceforstudent/(?P<pk>[0-9]+)/$', views.getattendanceforstudent),

]

urlpatterns = format_suffix_patterns(urlpatterns)