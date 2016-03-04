from rest_framework import serializers
from django.contrib.auth.models import User
from mywrapper.models import Subject, SubjectComponents,Student,Teacher, SubjectsPerStudent,SubjectsPerTeacher, Attendance,DaysAttendanceWasTaken,Test,Marks

class SubjectSerializer(serializers.ModelSerializer):
	id = serializers.ReadOnlyField()
	class Meta:
		model = Subject
		fields = ('id','subjectID')

class SubjectComponentsSerializer(serializers.ModelSerializer):
	subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())
	id = serializers.ReadOnlyField()
	class Meta:
		model = SubjectComponents
		fields = ('id','subject','sectionID','componentID')

class StudentSerializer(serializers.ModelSerializer):
	id = serializers.ReadOnlyField()
	class Meta:
		model = Student
		fields = ('id','studentID')

class TeacherSerializer(serializers.ModelSerializer):
	id = serializers.ReadOnlyField()
	class Meta:
		model = Teacher
		fields = ('id','teacherID')

class SubjectsPerTeacherSerializer(serializers.ModelSerializer):
	teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all())
	subjectComponents = serializers.PrimaryKeyRelatedField(queryset=SubjectComponents.objects.all())
	class Meta:
		model = SubjectsPerTeacher
		fields = ('teacher','subjectComponents')

class SubjectsPerStudentSerializer(serializers.ModelSerializer):
	student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
	subjectComponents = serializers.PrimaryKeyRelatedField(queryset=SubjectComponents.objects.all())
	class Meta:
		model = SubjectsPerStudent
		fields = ('student','subjectComponents')

class AttendanceSerializer(serializers.ModelSerializer):
	student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
	subjectComponents = serializers.PrimaryKeyRelatedField(queryset=SubjectComponents.objects.all())
	dateOfAttendance = serializers.DateField(input_formats = ('%d/%m/%Y',))
	class Meta:
		model = Attendance
		fields = ('student', 'subjectComponents', 'dateOfAttendance')

class DaysAttendanceWasTakenSerializer(serializers.ModelSerializer):
	dateOfAttendance = serializers.DateField(input_formats = ('%d/%m/%Y',))
	subjectComponents = serializers.PrimaryKeyRelatedField(queryset=SubjectComponents.objects.all())
	class Meta:
		model = DaysAttendanceWasTaken
		fields = ('subjectComponents', 'dateOfAttendance')

class TestSerializer(serializers.ModelSerializer):
	subjectComponents = serializers.PrimaryKeyRelatedField(queryset=SubjectComponents.objects.all())
	dateOfTest = serializers.DateField(input_formats = ('%d/%m/%Y',))
	class Meta:
		model = Test
		fields = ('subjectComponents','totalMarks','testType','dateOfTest')

class MarksSerializer(serializers.ModelSerializer):
	test = serializers.PrimaryKeyRelatedField(queryset=Test.objects.all())
	student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
	class Meta:
		model = Marks
		fields = ('student','test','studentMarks')

class UserSerializer(serializers.ModelSerializer):
	# notice = serializers.PrimaryKeyRelatedField(many=True, queryset=Notice.objects.all())
	class Meta:
		model = User
		fields = ('id', 'username')