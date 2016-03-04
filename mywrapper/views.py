from django.shortcuts import render

# Create your views here.
from mywrapper.models import Subject, SubjectComponents,Student,Teacher, SubjectsPerStudent,SubjectsPerTeacher, Attendance,DaysAttendanceWasTaken,Test,Marks
from mywrapper.serializers import SubjectSerializer, StudentSerializer, AttendanceSerializer,SubjectsPerStudentSerializer,TestSerializer, MarksSerializer,DaysAttendanceWasTakenSerializer,TeacherSerializer,SubjectsPerTeacherSerializer,SubjectComponentsSerializer
from rest_framework import generics
# from mywrapper.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions


class SubjectList(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectComponentsList(generics.ListCreateAPIView):
    queryset = SubjectComponents.objects.all()
    serializer_class = SubjectComponentsSerializer

class SubjectComponentsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubjectComponents.objects.all()
    serializer_class = SubjectComponentsSerializer

class SubjectsPerStudentList(generics.ListCreateAPIView):
    queryset = SubjectsPerStudent.objects.all()
    serializer_class = SubjectsPerStudentSerializer

class SubjectsPerStudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubjectsPerStudent.objects.all()
    serializer_class = SubjectsPerStudentSerializer

class SubjectsPerTeacherList(generics.ListCreateAPIView):
    queryset = SubjectsPerTeacher.objects.all()
    serializer_class = SubjectsPerTeacherSerializer

class SubjectsPerTeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubjectsPerTeacher.objects.all()
    serializer_class = SubjectsPerTeacherSerializer

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class AttendanceList(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class AttendanceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class TestList(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class TestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class MarksList(generics.ListCreateAPIView):
    queryset = Marks.objects.all()
    serializer_class = MarksSerializer

class MarksDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Marks.objects.all()
    serializer_class = MarksSerializer

class DaysAttendanceWasTakenList(generics.ListCreateAPIView):
    queryset = DaysAttendanceWasTaken.objects.all()
    serializer_class = DaysAttendanceWasTakenSerializer

class DaysAttendanceWasTakenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DaysAttendanceWasTaken.objects.all()
    serializer_class = DaysAttendanceWasTakenSerializer

# class NoticeList(generics.ListCreateAPIView):
#     queryset = Notice.objects.all()
#     serializer_class = NoticeSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     def perform_create(self, serializer):
#     	serializer.save(owner=self.request.user)


# class NoticeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Notice.objects.all()
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)a
#     serializer_class = NoticeSerializer

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer